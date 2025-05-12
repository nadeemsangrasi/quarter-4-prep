from fastapi import FastAPI, Body, Path
from models import UserCreate, CreateTask, ReadTask, ReadUser
from cruds import (
    get_users,
    create_user,
    get_single_user,
    create_task,
    get_tasks_by_user_id,
    get_single_task
)

app = FastAPI()

# -------------------- User Routes --------------------

@app.get("/users")
async def get_all_users():
    """Get all users."""
    return get_users()

@app.post("/users/register", response_model=ReadUser)
async def register_user(user: UserCreate = Body()) -> ReadUser:
    """Register a new user."""
    return create_user(user)
   
@app.get("/users/{user_id}", response_model=ReadUser)
async def get_user(user_id: int = Path(..., ge=1)) -> ReadUser:
    """Get a single user by user ID."""
    return get_single_user(user_id)

# -------------------- Task Routes --------------------

@app.post("/tasks/add/{user_id}", response_model=ReadTask)
async def add_task(user_id: int = Path(..., ge=1), task: CreateTask = Body()) -> ReadTask:
    """Add a new task for a user."""
    return create_task(user_id, task)

@app.get("/tasks/{user_id}", response_model=list[ReadTask])
async def get_all_tasks_by_users_id(user_id: int = Path(..., ge=1)) -> list[ReadTask]:
    """Get all tasks for a specific user."""
    return get_tasks_by_user_id(user_id)

@app.get("/tasks/task/{task_id}", response_model=ReadTask)
async def get_single_task_route(task_id: int = Path(..., ge=1)) -> ReadTask:
    """Get a single task by its ID."""
    return get_single_task(task_id)