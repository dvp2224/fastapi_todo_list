# FastAPI Basic To-Do Project

A simple To-Do List API built with FastAPI, featuring user authentication (JWT), CRUD operations, and in-memory storage. 

## Features
- **User Registration & Login** (JWT-based authentication)
- **Create, Read, Update, Delete (CRUD) To-Do Items**
- **Password Hashing** for secure storage
- **Protected Endpoints** (only authenticated users can manage To-Dos)
- **Swagger UI** for interactive API documentation

---

## Getting Started

### 1. Set Your Secret Key
Edit `security.py` and set your own `SECRET_KEY` value for JWT authentication. Use a strong, random string. Example:
```python
SECRET_KEY = "your-very-secret-key-here"
```

### 2. Install Requirements
```bash
pip install fastapi uvicorn passlib[bcrypt] python-jose
```

### 3. Run the API
```bash
uvicorn main1:app --reload
```

---

## API Usage

### Authentication Steps
1. **Register a User**
   - `POST /register/`
   - Body: `{ "username": "yourname", "password": "yourpassword" }`
2. **Login to Get Token**
   - `POST /token`
   - Form Data: `username`, `password`
   - Response: `{ "access_token": "...", "token_type": "bearer" }`
3. **Use Token for Authenticated Requests**
   - Add header: `Authorization: Bearer <access_token>`

---

## Example CURL Commands

### Register
```bash
curl -X POST "http://127.0.0.1:8000/register/" -H "Content-Type: application/json" -d '{"username":"user1","password":"pass123"}'
```

### Login (Get Token)
```bash
curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=user1&password=pass123"
```

### Create To-Do
```bash
curl -X POST "http://127.0.0.1:8000/todos/" -H "Authorization: Bearer <access_token>" -H "Content-Type: application/json" -d '{"task":"Buy groceries"}'
```

### Get All To-Dos
```bash
curl -X GET "http://127.0.0.1:8000/todos/" -H "Authorization: Bearer <access_token>"
```

### Update To-Do
```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" -H "Authorization: Bearer <access_token>" -H "Content-Type: application/json" -d '{"id":1,"task":"Buy groceries and cook","completed":true}'
```

### Delete To-Do
```bash
curl -X DELETE "http://127.0.0.1:8000/todos/1" -H "Authorization: Bearer <access_token>"
```

---

## Using Swagger UI
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
- You can interact with all endpoints, view models, and try requests directly.
- For protected endpoints, click "Authorize" and enter your token (from `/token`).

---

## Common Error Codes
- **400 Bad Request**: Invalid input, username already exists, or incorrect credentials.
- **401 Unauthorized**: Missing or invalid token, authentication failed.
- **404 Not Found**: To-Do item does not exist.

### Error Meanings
- **Username already registered**: Try a different username.
- **Incorrect username or password**: Check your credentials.
- **Could not validate credentials**: Token is missing, expired, or invalid.
- **To-Do item not found**: The requested item ID does not exist in the database.

---

## Notes
- This project uses in-memory storage; data will reset on server restart.
- For production, use a persistent database and environment variables for secrets.
