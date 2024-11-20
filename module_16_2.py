from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, который должен быть целым числом от 1 до 100",
            ge=1,
            le=100,
            example=1
        )
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя длиной от 5 до 20 символов",
            min_length=5,
            max_length=20,
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя от 18 до 120",
            ge=18,
            le=120,
            example=24
        )
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
