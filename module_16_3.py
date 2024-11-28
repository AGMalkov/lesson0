from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Инициализируем словарь users
users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users() -> dict:
    """
    Возвращает весь словарь users.
    """
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=24)
    ]
) -> str:
    """
    Добавляет нового пользователя в словарь.
    """
    new_user_id = str(int(max(users.keys(), key=int)) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        str,
        Path(description="Enter User ID", example="1")
    ],
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=28)
    ]
) -> str:
    """
    Обновляет информацию о пользователе с заданным user_id.
    """
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} does not exist"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        str,
        Path(description="Enter User ID to delete", example="2")
    ]
) -> str:
    """
    Удаляет пользователя с заданным user_id.
    """
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} does not exist"
