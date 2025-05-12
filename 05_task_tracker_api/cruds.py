from fastapi import HTTPException
from models import ReadUser, ReadTask, CreateTask,UserCreate
import random

users: list[dict[str, str | int]] = []
tasks: list[dict] = []

def get_users() -> list[ReadUser]:
    """
    Retrieve all users.
    Raises 404 if no users are found.
    """
    if len(users) == 0:
        raise HTTPException(
            status_code=404, detail="users not found")
    return [
        ReadUser(
            id=user["id"],
            username=user["username"],
            name=user["name"],
            age=user["age"],
            email=user["email"]
        ) for user in users
    ]

def create_user(user: UserCreate) -> ReadUser:
    """
    Create a new user.
    Raises 400 if user with same email or username exists.
    """
    user_id = random.randint(111, 999)
    new_user = {
        "id": user_id,
        "username": user.username,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    for u in users:
        if new_user["email"] == u["email"] or new_user["username"] == u["username"]:
            raise HTTPException(
                status_code=400, detail="user already exists"
            )
    users.append(new_user)
    return ReadUser(
        id=new_user["id"],
        username=new_user["username"],
        name=new_user["name"],
        age=new_user["age"],
        email=new_user["email"]
    )

def get_single_user(user_id: int) -> ReadUser:
    """
    Retrieve a single user by user_id.
    Raises 404 if user is not found.
    """
    user = next(filter(lambda x: x["id"] == user_id, users), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return ReadUser(
        id=user["id"],
        username=user["username"],
        name=user["name"],
        age=user["age"],
        email=user["email"]
    )

def create_task(user_id: int, task: CreateTask) -> ReadTask:
    """
    Create a new task for a user.
    Raises 404 if user does not exist.
    """
    is_user_exist = next(filter(lambda x: x["id"] == user_id, users), None)
    if not is_user_exist:
        raise HTTPException(status_code=404, detail="user not found first register user please")
    task_id = random.randint(111, 999)
    new_task = {
        "id": task_id,
        "user_id": user_id,
        "title": task.title,
        "description": task.description
    }
    tasks.append(new_task)
    return ReadTask(
        id=task_id,
        user_id=user_id,
        title=task.title,
        description=task.description
    )

def get_single_task(task_id: int) -> ReadTask:
    """
    Retrieve a single task by task_id.
    Raises 404 if task is not found.
    """
    task = next(filter(lambda x: x["id"] == task_id, tasks), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return ReadTask(
        id=task["id"],
        user_id=task["user_id"],
        title=task["title"],
        description=task["description"]
    )

def get_tasks_by_user_id(user_id: int) -> list[ReadTask]:
    """
    Retrieve all tasks for a specific user.
    Raises 404 if no tasks are found for the user.
    """
    is_task = next(filter(lambda x: x["user_id"] == user_id, tasks), None)
    if not is_task:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return [
        ReadTask(
            id=task["id"],
            user_id=task["user_id"],
            title=task["title"],
            description=task["description"]
        ) for task in tasks if task["user_id"] == user_id
    ]