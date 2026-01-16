# FastAPI Learning Project

A comprehensive FastAPI application demonstrating RESTful API development with structured routing, Pydantic models, and automatic API documentation.

## 📁 Project Structure

```
FastAPI/
├── 01/                 # Basic FastAPI setup
│   └── main.py
├── 02/                 # Intermediate setup with models
│   └── main.py
│   └── models/
└── 03/                 # Full application with routers
    ├── main.py
    ├── models/
    │   ├── item.py     # Item data models
    │   └── user.py     # User data models
    └── routers/
        ├── items.py    # Item endpoints
        └── users.py    # User endpoints
```

## 🚀 Features

- **RESTful API** with full CRUD operations for Users and Items
- **Automatic API Documentation** (Swagger UI and ReDoc)
- **Data Validation** using Pydantic models
- **Structured Routing** with separate router modules
- **HTTP Status Codes** and error handling
- **Response Models** for clean API responses

## 📋 Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (with email-validator for email validation)

## 🔧 Installation

1. Clone or navigate to the project directory:
```bash
cd c:\Users\sonrisa\dolgok\python\FastAPI
```

2. Install dependencies:
```bash
pip install fastapi uvicorn pydantic[email]
```

## ▶️ Running the Application

### Running Version 03 (Full Application)

```bash
cd 03
uvicorn main:app --reload
```

The server will start at: `http://localhost:8000`


## 📚 API Documentation

FastAPI automatically generates interactive API documentation:

### **Swagger UI (Interactive)**
Visit: **`http://localhost:8000/docs`**

Features:
- ✨ Interactive API explorer
- 🧪 Test endpoints directly in the browser
- 📝 Automatic request/response examples
- 🔍 Schema definitions for all models
- 📋 Try out API calls with custom parameters

### **ReDoc (Alternative)**
Visit: **`http://localhost:8000/redoc`**

Features:
- 📖 Clean, three-panel documentation
- 🎨 Beautiful, responsive design
- 📊 Detailed schema documentation

### **OpenAPI Schema (JSON)**
Visit: **`http://localhost:8000/openapi.json`**

Raw OpenAPI 3.0 specification for API integration and code generation.

## 🔌 API Endpoints

### Root
- `GET /` - Welcome message

### Users (`/users`)
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `POST /users/` - Create a new user
- `PUT /users/{user_id}` - Update user by ID
- `DELETE /users/{user_id}` - Delete user by ID

### Items (`/items`)
- `GET /items/` - Get all items
- `GET /items/{item_id}` - Get item by ID
- `POST /items/` - Create a new item
- `PUT /items/{item_id}` - Update item by ID
- `DELETE /items/{item_id}` - Delete item by ID

## 🧪 Testing the API

With the server running (`uvicorn main:app --reload` in the 03 directory), you can test the API using the following methods:

### Using cURL Commands

#### Test Root Endpoint
```bash
curl http://localhost:8000/
```

#### Get All Users
```bash
curl http://localhost:8000/users/
```

#### Get User by ID
```bash
curl http://localhost:8000/users/1
```

#### Create New User
```bash
curl -X POST http://localhost:8000/users/ ^
  -H "Content-Type: application/json" ^
  -d "{\"id\": 10, \"username\": \"new_user\", \"email\": \"newuser@example.com\", \"full_name\": \"New User\", \"is_active\": true}"
```

#### Update User
```bash
curl -X PUT http://localhost:8000/users/1 ^
  -H "Content-Type: application/json" ^
  -d "{\"id\": 1, \"username\": \"john_doe_updated\", \"email\": \"john.updated@example.com\", \"full_name\": \"John Doe Updated\", \"is_active\": true}"
```

#### Delete User
```bash
curl -X DELETE http://localhost:8000/users/3
```

#### Get All Items
```bash
curl http://localhost:8000/items/
```

#### Get Item by ID
```bash
curl http://localhost:8000/items/1
```

#### Create New Item
```bash
curl -X POST http://localhost:8000/items/ ^
  -H "Content-Type: application/json" ^
  -d "{\"id\": 10, \"name\": \"New Item\", \"description\": \"A brand new item\", \"price\": 49.99}"
```

### Using PowerShell (Windows)

```powershell
# Test root endpoint
Invoke-RestMethod -Uri "http://localhost:8000/" -Method Get

# Get all users
Invoke-RestMethod -Uri "http://localhost:8000/users/" -Method Get

# Get user by ID
Invoke-RestMethod -Uri "http://localhost:8000/users/1" -Method Get

# Create new user
$user = @{
    id = 10
    username = "new_user"
    email = "newuser@example.com"
    full_name = "New User"
    is_active = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/users/" -Method Post -Body $user -ContentType "application/json"

# Get all items
Invoke-RestMethod -Uri "http://localhost:8000/items/" -Method Get
```

## 📦 Data Models

### User Model
```python
{
    "id": int,
    "username": str (3-50 chars),
    "email": str (valid email),
    "full_name": str (optional, max 100 chars),
    "is_active": bool (default: true)
}
```

### Item Model
```python
{
    "id": int,
    "name": str,
    "description": str (optional),
    "price": float
}
```

## 🎓 Learning Progression

### 01 - Basic Setup
Simple FastAPI application with inline routes

### 02 - Adding Models
Introduction of Pydantic models for data validation

### 03 - Full Structure
- Separated routers for different resources
- Organized models in separate files
- Complete CRUD operations
- Error handling and HTTP status codes

## 🤝 Contributing

This is a learning project. Feel free to experiment with:
- Adding authentication
- Implementing a real database (SQLAlchemy, MongoDB)
- Adding query parameters and filtering
- Implementing pagination
- Adding background tasks

## 📝 License

This is a learning project for educational purposes.

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

---

**Happy Coding! 🚀**
