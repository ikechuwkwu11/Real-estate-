# 🏘️ Real Estate Web App (Flask)
A lightweight, functional real estate web application built with Flask, Flask-Login, and SQLAlchemy. Users can register, log in, view available properties, and simulate property purchases with the generation of a one-time access code for each purchase.

## 🚀 Features
👤 User Authentication
- User Registration and Login
- Session management using Flask-Login
- Protected Routes to restrict access to authenticated users

## 🏠 Property Management
- View all available property listings
- Simulate buying a property
- Generate a unique one-time access code per purchase

## 🛠 Tech Stack
| Layer      | Technology              |
| ---------- | ----------------------- |
| Backend    | Python, Flask           |
| Database   | SQLite + SQLAlchemy ORM |
| Auth       | Flask-Login             |
| Forms      | WTForms (optional)      |
| Templating | Jinja2                  |
| Styling    | Bootstrap (optional)    |



## 🧪 Requirements
- Flask
- Flask-Login
- Flask-SQLAlchemy
- WTForms (if using form.py)

## 💻 Usage
- Access the Web App
- Register at: http://127.0.0.1:5000/register
- Login at: http://127.0.0.1:5000/login
- Browse properties at: /dashboard
- Click to "buy" a property and receive a unique access code
- Logout via /logout

## 🔒 Security Notice
⚠️ User passwords are currently stored in plaintext
It is strongly recommended to implement password hashing using werkzeug.security or similar.

## ✅ To-Do
- Add admin dashboard for managing property listings
- Hash and securely store user passwords
- Add styling using Bootstrap or custom CSS
- Deploy to a platform like Render, Railway, or Heroku
