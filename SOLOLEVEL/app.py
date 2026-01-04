import os
import json
import re
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

# --- CONFIGURATION ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sololevel-secret-key-999' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sololevel.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- DATABASE MODEL ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data = db.Column(db.Text, default='{"habits": [{"id":1, "name":"Daily Workout", "diff":2}, {"id":2, "name":"Read Grimoire", "diff":1.5}], "records": {}, "user": {"xp":0, "hp":100, "lastLogin": null, "currentStreak":0}, "isDark": true}')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- ROUTES ---

@app.route('/')
def root():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Username or Password.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 1. Check Username Length
        if len(username) < 5:
            flash('Username must be at least 5 characters.')
            return redirect(url_for('register'))

        # 2. Check Password Special Char
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            flash('Password must contain at least one special character (!@#$).')
            return redirect(url_for('register'))

        # 3. Check if Username Taken
        exists = User.query.filter_by(username=username).first()
        if exists:
            flash('Username already taken. Choose another.')
            return redirect(url_for('register'))

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        
        flash('Account Created! Please Login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/api/data', methods=['GET', 'POST'])
@login_required
def api_data():
    if request.method == 'GET':
        return current_user.data
    else:
        current_user.data = json.dumps(request.json)
        db.session.commit()
        return jsonify({"status": "saved"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)