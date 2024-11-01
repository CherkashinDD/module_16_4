from fastapi import FastAPI, Body, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_user(message: User) -> str:
    message.id = len(users) + 1
    users.append(message)
    return f"id: {message.id}, username: {message.username}, age: {message.age}"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, usname: str = Body(), ag: int = Body()) -> str:
    try:
        edit_message = users[user_id - 1]
        edit_message.username = usname
        edit_message.age = ag
        return f"id: {edit_message.id}, username: {edit_message.username}, age: {edit_message.age}"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        user_del = users.pop(user_id - 1)
        return f"id: {user_del.id}, username: {user_del.username}, age: {user_del.age}"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
