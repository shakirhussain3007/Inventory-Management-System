# Inventory Management System

A modern Inventory Management System built with **FastAPI**, **SQLAlchemy**, and **MySQL** following a layered architecture. The project provides secure authentication using JWT, database migrations with Alembic, and a clean RESTful API structure.

---

## Features

- User Authentication with JWT
- Password Hashing using Bcrypt
- Layered Architecture
- CRUD Operations
- MySQL Database Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- Environment Variable Configuration
- Interactive API Documentation
- Input Validation using Pydantic

---

## Tech Stack

- FastAPI
- Python
- SQLAlchemy
- MySQL
- Alembic
- Pydantic
- JWT (python-jose)
- Passlib
- Bcrypt
- Uvicorn

---

## Project Structure

```
Inventory-Management-System/
│
├── app/
│   ├── config/
│   ├── controllers/
│   ├── middlewares/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── alembic/
├── migrations/
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Inventory-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=inventory_db
DB_USER=your_username
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Database Migration

```bash
alembic upgrade head
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Security

- JWT Authentication
- Password Hashing with Bcrypt
- Environment Variables for Sensitive Data

---

## Future Improvements

- Role-Based Access Control (RBAC)
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Inventory Reports
- Email Notifications

---

## Author

**Shakir Hussain**

Backend Developer | Python | FastAPI | SQLAlchemy | MySQL
