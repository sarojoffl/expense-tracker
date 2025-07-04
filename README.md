# Django Expense Tracker API

## 🚀 Project Overview

A RESTful API for tracking personal expenses and incomes with user authentication, tax calculation, and full CRUD functionality.

---

## 🚀 Features

- 🔐 JWT Authentication (Login, Register, Refresh)
- 🧾 Expense & Income record management
- 🧮 Automatic tax calculation (flat or percentage)
- 🔄 Full CRUD operations
- 🔍 Paginated responses
- 🔒 Role-based access (user vs. superuser)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sarojoffl/expense-tracker.git
cd expense-tracker
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```

---


## 📌 API Endpoint Documentation

### 🔐 Authentication Endpoints

| Method | Endpoint              | Description         |
|--------|-----------------------|---------------------|
| POST   | /api/auth/register/   | Register a new user |
| POST   | /api/auth/login/      | Obtain JWT tokens   |
| POST   | /api/auth/refresh/    | Refresh access token|

---

### 💼 Expense/Income Endpoints

| Method | Endpoint                | Description                            |
|--------|-------------------------|----------------------------------------|
| GET    | /api/expenses/          | List current user's records (paginated)|
| POST   | /api/expenses/          | Create a new expense/income record     |
| GET    | /api/expenses/{id}/     | Retrieve a specific record             |
| PUT    | /api/expenses/{id}/     | Update a specific record               |
| DELETE | /api/expenses/{id}/     | Delete a specific record               |

---

## 📦 Sample API Requests & Responses

---

### 🧑‍💻 Register User

**POST /api/auth/register/**

**Request:**
```json
{
    "username": "saroj123",
    "email": "saroj@example.com",
    "password": "securepassword"
}
```

**Response:**
```json
{
    "username": "saroj123",
    "email": "saroj@example.com"
}
```

### 🔐 Login User
**POST /api/auth/login/**

**Request:**
```json
{
    "username": "saroj123",
    "password": "securepassword"
}
```

**Response:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```

### 🧾 Create Expense Record
**POST /api/expenses/**
```bash
Authorization: Bearer <access_token>
```

**Request:**
```json
{
    "title": "Lunch",
    "description": "Business lunch with client",
    "amount": 50.00,
    "transaction_type": "debit",
    "tax": 5.00,
    "tax_type": "flat"
}
```

**Response:**
```json
{
    "id": 4,
    "total": 55.0,
    "title": "Lunch",
    "description": "Business lunch with client",
    "amount": "50.00",
    "transaction_type": "debit",
    "tax": "5.00",
    "tax_type": "flat",
    "created_at": "2025-07-04T19:40:22.361813Z",
    "updated_at": "2025-07-04T19:40:22.361813Z",
    "user": 4
}
```

### 📋 List User's Records (Paginated)
**GET /api/expenses/**
```bash
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "total": 55.0,
            "title": "Lunch",
            "description": "Business lunch with client",
            "amount": "50.00",
            "transaction_type": "debit",
            "tax": "5.00",
            "tax_type": "flat",
            "created_at": "2025-07-04T19:40:22.361813Z",
            "updated_at": "2025-07-04T19:40:22.361813Z",
            "user": 4
        }
    ]
}
```

### 🧾 Retrieve Single Record
**GET /api/expenses/4/**
```bash
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "id": 4,
    "total": 55.0,
    "title": "Lunch",
    "description": "Business lunch with client",
    "amount": "50.00",
    "transaction_type": "debit",
    "tax": "5.00",
    "tax_type": "flat",
    "created_at": "2025-07-04T19:40:22.361813Z",
    "updated_at": "2025-07-04T19:40:22.361813Z",
    "user": 4
}
```

### ♻️ Update Record
**PUT /api/expenses/4/**
```bash
Authorization: Bearer <access_token>
```

**Request:**
```json
{
    "title": "Client Lunch",
    "description": "Updated description",
    "amount": 60.00,
    "transaction_type": "debit",
    "tax": 10.00,
    "tax_type": "percentage"
}
```

**Response:**
```json
{
    "id": 4,
    "total": 66.0,
    "title": "Client Lunch",
    "description": "Updated description",
    "amount": "60.00",
    "transaction_type": "debit",
    "tax": "10.00",
    "tax_type": "percentage",
    "created_at": "2025-07-04T19:40:22.361813Z",
    "updated_at": "2025-07-04T19:49:52.185943Z",
    "user": 4
}
```

### 🗑️ Delete Record
**DELETE /api/expenses/4/**
```bash
Authorization: Bearer <access_token>
```

**Response:**
<pre> 204 No Content </pre>

## 🧪 Testing Checklist

- ✅ Register and login using JWT
- ✅ Access protected endpoints with token
- ✅ Create, retrieve, update, and delete records
- ✅ Verify total amount with flat/percentage tax
- ✅ Ensure regular users can't access other users' records
- ✅ Superuser can access all records
- ✅ Invalid or unauthenticated requests return correct errors

## 🔒 Permissions

- 🔹 **Regular users**: Can access and manage their own records only
- 🔹 **Superusers**: Can access all users' records
- 🔹 **Authentication**: Required via JWT token

## ❗ Common Errors & Fixes

- `401 Unauthorized`: Make sure to include the JWT token in `Authorization` header
- `403 Forbidden`: You tried to access someone else's record
- `400 Bad Request`: Invalid input data — check required fields

## 🧑‍💻 Author

Saroj
📧 sarojoffl@gmail.com
🌐 [github.com/sarojoffl](https://github.com/sarojoffl)

## 📄 License

This project is for educational use during the internship task at [**Vrit Technologies**](https://vrittechnologies.com/).
