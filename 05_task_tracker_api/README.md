# Task Tracker API - Guide

This document describes all available API endpoints, including request/response formats and error responses.

---

## User Endpoints

### 1. Get All Users

- **Endpoint:** `GET /users`
- **Response:**
  ```json
  [
    {
      "id": 123,
      "name": "John Doe",
      "username": "johndoe",
      "email": "john@example.com",
      "age": 25
    }
    // ...more users
  ]
  ```
- **Error Response:**
  - `404 Not Found`
    ```json
    { "detail": "users not found" }
    ```

---

### 2. Register User

- **Endpoint:** `POST /users/register`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "age": 25
  }
  ```
  - `name`: string, 2-40 chars
  - `username`: string, 3-50 chars, lowercase, unique
  - `email`: valid email, unique
  - `age`: integer (optional)
- **Response:**
  ```json
  {
    "id": 123,
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "age": 25
  }
  ```
- **Error Responses:**
  - `400 Bad Request` (duplicate email/username)
    ```json
    { "detail": "user already exists" }
    ```
  - `422 Unprocessable Entity` (validation errors)
    ```json
    {
      "detail": [
        {
          "loc": ["body", "name"],
          "msg": "Name must be at least 2 characters long",
          "type": "value_error"
        }
      ]
    }
    ```

---

### 3. Get Single User

- **Endpoint:** `GET /users/{user_id}`
- **Response:**
  ```json
  {
    "id": 123,
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "age": 25
  }
  ```
- **Error Response:**
  - `404 Not Found`
    ```json
    { "detail": "User not found" }
    ```

---

## Task Endpoints

### 4. Add Task for User

- **Endpoint:** `POST /tasks/add/{user_id}`
- **Request Body:**
  ```json
  {
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs"
  }
  ```
  - `title`: string, 3-100 chars
  - `description`: string, 1-500 chars
- **Response:**
  ```json
  {
    "id": 456,
    "user_id": 123,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs"
  }
  ```
- **Error Responses:**
  - `404 Not Found` (user does not exist)
    ```json
    { "detail": "user not found first register user please" }
    ```
  - `422 Unprocessable Entity` (validation errors)
    ```json
    {
      "detail": [
        {
          "loc": ["body", "title"],
          "msg": "Title must be at least 3 characters long",
          "type": "value_error"
        }
      ]
    }
    ```

---

### 5. Get All Tasks by User

- **Endpoint:** `GET /tasks/{user_id}`
- **Response:**
  ```json
  [
    {
      "id": 456,
      "user_id": 123,
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs"
    }
    // ...more tasks
  ]
  ```
- **Error Response:**
  - `404 Not Found`
    ```json
    { "detail": "Tasks not found" }
    ```

---

### 6. Get Single Task

- **Endpoint:** `GET /tasks/task/{task_id}`
- **Response:**
  ```json
  {
    "id": 456,
    "user_id": 123,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs"
  }
  ```
- **Error Response:**
  - `404 Not Found`
    ```json
    { "detail": "Task not found" }
    ```

---

## Validation Error Example

- **Status:** `422 Unprocessable Entity`
- **Example:**
  ```json
  {
    "detail": [
      {
        "loc": ["body", "field_name"],
        "msg": "Error message",
        "type": "value_error"
      }
    ]
  }
  ```

---

## Notes

- All endpoints return JSON.
- All errors follow the FastAPI error format.
- All IDs are integers.
- All string fields are trimmed and validated as described above.
