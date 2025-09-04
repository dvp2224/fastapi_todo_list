from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List

# Create FastAPI instance
app = FastAPI()

# Pydantic model with validation for a To-Do item
class ToDoItem(BaseModel):
    id: int = Field(default=None)  # ID is optional on creation
    task: str = Field(min_length=5, max_length=100) # Task must be between 5 and 100 characters
    completed: bool = False

# In-memory "database" to store our To-Do items
db: Dict[int, ToDoItem] = {}
next_id = 1

# Root endpoint to confirm the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

# --- CRUD Operations ---

# CREATE: Add a new task
@app.post("/todos/", response_model=ToDoItem)
def create_todo(item: ToDoItem):
    global next_id
    item.id = next_id
    db[next_id] = item
    next_id += 1
    return item

# READ: Get all tasks
@app.get("/todos/", response_model=List[ToDoItem])
def get_all_todos():
    return list(db.values())

# READ: Get a single task by ID
@app.get("/todos/{todo_id}", response_model=ToDoItem)
def get_todo_by_id(todo_id: int):
    if todo_id not in db:
        # Custom error handling for an item that does not exist
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return db[todo_id]

# UPDATE: Update an existing task
@app.put("/todos/{todo_id}", response_model=ToDoItem)
def update_todo(todo_id: int, updated_item: ToDoItem):
    if todo_id not in db:
        # Custom error handling for an item that does not exist
        raise HTTPException(status_code=404, detail="To-Do item not found")
    db[todo_id] = updated_item
    return updated_item

# DELETE: Delete a task
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todo_id not in db:
        # Custom error handling for an item that does not exist
        raise HTTPException(status_code=404, detail="To-Do item not found")
    del db[todo_id]
    return