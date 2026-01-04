# ⚔️ Solo Leveling Habit Tracker ( The System )

> **"You have been chosen as a Player."**

![Project Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Deployment](https://img.shields.io/badge/Hosted%20on-PythonAnywhere-blueviolet)

## 📖 About The Project

Welcome to the **Solo Leveling Habit Tracker**, a gamified productivity application inspired by the "System" interface from the hit manhwa/anime *Solo Leveling*.

This application turns your daily life into a RPG. Instead of boring to-do lists, you complete **"Daily Quests"** to earn **XP**, maintain your **HP (Health)**, and raise your **Rank** from an E-Rank weakling to The Monarch.

Currently, the project features the core design structure, UI/UX, and database connectivity, hosted live on **PythonAnywhere**.

---

## ✨ Key Features

### 📊 The System Dashboard
- **Real-time Analytics:** View your productivity stats via dynamic Bar Graphs and Charts.
- **Activity Heatmap:** A visual representation of your consistency (similar to GitHub contributions), showing your "Dungeon Clear" history.
- **Health & XP:** Missing habits damages your Health (HP). Completing them grants XP to Level Up.

### 🏆 Gamification Mechanics
- **Ranking System:**
  - Start as **E-Rank**.
  - Grind XP to promote to **D, C, B, A, S**, and finally **The Monarch**.
- **Streaks:**
  - **Individual Streak:** Track consistency for specific habits.
  - **Overall Streak:** Your total days of perfect "Daily Quest" completion.

### 🔊 Immersive Experience
- **Sound Effects:** Custom SFX for leveling up, completing tasks, and clicking (mapped in `static/sound1.mp3` etc.).
- **Solo Leveling UI:** Dark-themed, sleek interface mimicking the manhwa's system windows.

### 🔐 Gatekeeper (Authentication)
- Secure **Login** and **Registration** pages to save your progress and player data.

---

## 📂 Project Structure

This project is built using **Flask (Python)** with a lightweight **SQLite** database.

```text
Solo-Leveling-Tracker/
├── instance/
│   └── sololevel.db       # SQLite Database (Player Stats, Habits, User Data)
├── static/
│   ├── sound1.mp3         # SFX: Task Complete
│   ├── sound2.mp3         # SFX: Level Up
│   ├── sound3.mp3         # SFX: UI Click
│   ├── sound4.mp3         # SFX: Error/Damage
│   ├── sound5.mp3         # SFX: Rank Up
│   ├── style.css          # (Implied) Stylesheets
│   └── script.js          # (Implied) Chart logic & Interactions
├── templates/
│   ├── index.html         # Main Dashboard (The System Interface)
│   ├── login.html         # Player Login
│   └── register.html      # Player Awakening (Registration)
├── app.py                 # Main Application Logic (Flask)
└── README.md              # Documentation
