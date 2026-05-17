> 🚧 This project is currently under development
# Secure Task Manager

A fullstack task management web application that allows users to manage their daily tasks with authentication and secure data handling.

---

## Purpose

This project was built to practice fullstack development, including backend APIs, authentication, and frontend state management.

It simulates a real-world task management system where each user has private data and secure access.

---

## Features

- User registration and login
- Secure authentication (hashed passwords using bcrypt)
- Create, update, and delete tasks
- Mark tasks as completed
- Filter tasks (active / completed)
- User-specific task isolation

---

## Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- React
- CSS

**Database**
- SQLite

**Other**
- Git

---

## Architecture

Client (React)  
↓  
REST API (Flask)  
↓  
Database (SQLite)  

- The frontend communicates with the backend via REST API  
- The backend handles authentication and business logic  
- Data is stored per user in the database  

---

## How It Works (Flow)

1. User registers or logs in  
2. Authentication is handled by the backend  
3. User creates tasks via the UI  
4. Tasks are stored in the database  
5. The frontend updates dynamically based on API responses  

---

## API Endpoints (Bonus - חשוב מאוד)

| Method | Endpoint     | Description             |
|--------|-------------|--------------------------|
| POST   | /register   | Create new user          |
| POST   | /login      | Authenticate user        |
| GET    | /tasks      | Get user tasks           |
| POST   | /tasks      | Create new task          |
| PUT    | /tasks/:id  | Update task              |
| DELETE | /tasks/:id  | Delete task              |

---

## Screenshots

### Login Page
![Login](./screenshots/login.png)

### Dashboard
![Dashboard](./screenshots/dashboard.png)

---

## Installation

### Backend

cd backend  
pip install -r requirements.txt  
python app.py  

### Frontend

cd frontend  
npm install  
npm start  

---

## Security

- Passwords are hashed using bcrypt  
- Users can only access their own tasks  
- Input validation is implemented on both client and server  

---

## Future Improvements

- Add JWT authentication  
- Deploy to cloud  
- Add notifications  
- Improve UI/UX  

---

## What I Learned

- Building REST APIs with Flask  
- Managing frontend state in React  
- Implementing authentication and user-based access control  
