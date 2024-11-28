from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Annotated, List

app = FastAPI()

# Модель пользователя
class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    age: int = Field(..., ge=18, le=120, description="Enter age", example=24)

# Список пользователей
users: List[User] = []

@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    """
    Возвращает список пользователей.
    """
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=24)
    ]
) -> User:
    """
    Создает нового пользователя и добавляет его в список.
    """
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: Annotated[
        int,
        Path(ge=1, description="Enter User ID", example=1)
    ],
    username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")
    ],
    age: Annotated[
        int,
        Path(ge=18, le=120, description="Enter age", example=28)
    ]
) -> User:
    """
    Обновляет данные пользователя по user_id.
    """
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: Annotated[
        int,
        Path(ge=1, description="Enter User ID", example=1)
    ]
) -> User:
    """
    Удаляет пользователя по user_id.
    """
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
