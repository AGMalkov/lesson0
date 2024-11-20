from fastapi import FastAPI

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    new_user_id = str(int(max(users.keys(), key=int)) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} does not exist"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} does not exist"
