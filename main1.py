from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict, List
from security import create_access_token, verify_password, get_password_hash, get_current_user

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic models for users
class UserInDB(BaseModel):
    username: str
    hashed_password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Pydantic model with validation for a To-Do item
class ToDoItem(BaseModel):
    id: int
    task: str = Field(min_length=5, max_length=100) # Task must be between 5 and 100 characters
    completed: bool = False

# Pydantic model for creating a To-Do item (without ID)
class ToDoCreate(BaseModel):
    task: str = Field(min_length=5, max_length=100) # Task must be between 5 and 100 characters
    completed: bool = False

# In-memory "databases"
db: Dict[int, ToDoItem] = {}
next_id = 1
users_db = {}

# Root endpoint to confirm the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

# --- Authentication Endpoints ---

@app.post("/register/")
def register_user(user: UserLogin):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = UserInDB(username=user.username, hashed_password=hashed_password)
    return {"message": "User registered successfully"}

@app.post("/token")
def login_for_access_token(form_data: UserLogin):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- CRUD Operations ---

# CREATE: Add a new task
@app.post("/todos/", response_model=ToDoItem)
def create_todo(item: ToDoCreate, current_user: dict = Depends(get_current_user)):
    global next_id
    new_todo = ToDoItem(id=next_id, task=item.task, completed=item.completed)
    db[next_id] = new_todo
    next_id += 1
    return new_todo

# READ: Get all tasks
@app.get("/todos/", response_model=List[ToDoItem])
def get_all_todos(current_user: dict = Depends(get_current_user)):
    return list(db.values())

# READ: Get a single task by ID
@app.get("/todos/{todo_id}", response_model=ToDoItem)
def get_todo_by_id(todo_id: int, current_user: dict = Depends(get_current_user)):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return db[todo_id]

# UPDATE: Update an existing task
@app.put("/todos/{todo_id}", response_model=ToDoItem)
def update_todo(todo_id: int, updated_item: ToDoItem, current_user: dict = Depends(get_current_user)):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    # Ensure the ID in the URL matches the ID in the body
    updated_item.id = todo_id
    db[todo_id] = updated_item
    return updated_item

# DELETE: Delete a task
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, current_user: dict = Depends(get_current_user)):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    del db[todo_id]
    return