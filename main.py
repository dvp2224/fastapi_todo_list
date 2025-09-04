from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

# Create FastAPI instance
app = FastAPI()

# A Pydantic model for the To-Do item
class ToDoItem(BaseModel):
    id: int
    task: str
    completed: bool = False

# In-memory "database"
# Use Dict[int, ToDoItem] for type hinting
db: Dict[int, ToDoItem] = {}
next_id = 1

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

# --- CRUD Operations ---

# CREATE: Add a new task
@app.post("/todos/")
def create_todo(task: str):
    global next_id
    new_todo = ToDoItem(id=next_id, task=task)
    db[next_id] = new_todo
    next_id += 1
    return new_todo

# READ: Get all tasks
@app.get("/todos/", response_model=List[ToDoItem])
def get_all_todos():
    return list(db.values())

# READ: Get a single task by ID
@app.get("/todos/{todo_id}", response_model=ToDoItem)
def get_todo_by_id(todo_id: int):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return db[todo_id]

# UPDATE: Update an existing task
@app.put("/todos/{todo_id}", response_model=ToDoItem)
def update_todo(todo_id: int, updated_item: ToDoItem):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    db[todo_id] = updated_item
    return updated_item

# DELETE: Delete a task
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    del db[todo_id]
    return