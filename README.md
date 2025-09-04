# To-Do List API with FastAPI 📝

This is a simple To-Do List API built with FastAPI, demonstrating core concepts like **CRUD operations**, **data validation**, and **user authentication** using JWTs. The project uses an in-memory dictionary as a temporary database for learning purposes.


## Features

  - **User Authentication**: Secure your API endpoints with a registration and login system that generates JSON Web Tokens (JWTs).
  - **Data Validation**: Utilizes Pydantic models to validate incoming data, ensuring it meets specified criteria (e.g., minimum character length).
  - **Error Handling**: Returns clear, custom error messages for scenarios like a user trying to access a resource that doesn't exist.
  - **CRUD Operations**: A complete set of endpoints to **C**reate, **R**ead, **U**pdate, and **D**elete to-do items.


## Getting Started

### 1\. **Prerequisites**

Ensure you have **Python 3.7+** installed.

### 2\. **Installation**

Clone the repository and install the required dependencies:

```bash
pip install "fastapi[all]" "passlib[bcrypt]" python-jose
```

### 3\. **Run the Server**

Start the FastAPI server. If your main file is named `main.py`, use this command:

```bash
uvicorn main:app --reload
```

If you saved it as `main1.py`, use:

```bash
uvicorn main1:app --reload
```

The API will be available at `http://127.0.0.1:8000`.


## API Documentation

FastAPI automatically generates interactive documentation.

  * **Swagger UI**: `http://127.0.0.1:8000/docs`
  * **ReDoc**: `http://127.0.0.1:8000/redoc`

Use Swagger UI to test all endpoints interactively.


## Endpoints and cURL Commands

### 1\. **User Authentication**

You **must** perform these steps first to get an access token for the protected endpoints.

  * **Register a user**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/register/" \
    -H "Content-Type: application/json" \
    -d '{"username": "testuser", "password": "securepassword"}'
    ```
  * **Log in and get a token**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/token" \
    -H "Content-Type: application/json" \
    -d '{"username": "testuser", "password": "securepassword"}'
    ```
    This command returns a JWT (access token) and its type. You will need this token for all subsequent requests.


### 2\. **To-Do List Operations**

To access these, you must include your JWT in the `Authorization` header.

  * **Create a To-Do Item** (`POST /todos/`)

    ```bash
    curl -X POST "http://127.0.0.1:8000/todos/" \
    -H "Authorization: Bearer <your_access_token>" \
    -H "Content-Type: application/json" \
    -d '{"task": "Learn FastAPI and build a project"}'
    ```

  * **Get All To-Do Items** (`GET /todos/`)

    ```bash
    curl -X GET "http://127.0.0.1:8000/todos/" \
    -H "Authorization: Bearer <your_access_token>"
    ```

  * **Get a Single To-Do Item** (`GET /todos/{todo_id}`)

    ```bash
    curl -X GET "http://127.0.0.1:8000/todos/1" \
    -H "Authorization: Bearer <your_access_token>"
    ```

  * **Update a To-Do Item** (`PUT /todos/{todo_id}`)

    ```bash
    curl -X PUT "http://127.0.0.1:8000/todos/1" \
    -H "Authorization: Bearer <your_access_token>" \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "task": "Learn and apply FastAPI", "completed": true}'
    ```

  * **Delete a To-Do Item** (`DELETE /todos/{todo_id}`)

    ```bash
    curl -X DELETE "http://127.0.0.1:8000/todos/1" \
    -H "Authorization: Bearer <your_access_token>"
    ```


## Common Error Codes

| Status Code | Description | Example Scenario |
| :--- | :--- | :--- |
| **401 Unauthorized** | The request is missing a valid JWT or the token is invalid. | Trying to access a protected endpoint without logging in. |
| **404 Not Found** | The requested resource does not exist. | Trying to access a to-do item with an ID that has been deleted. |
| **422 Unprocessable Entity** | The request body is improperly formatted or fails validation checks. | Submitting a new task with a name shorter than 5 characters. |
