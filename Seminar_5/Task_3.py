# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
# ●	Создайте модуль приложения и настройте сервер и маршрутизацию.
# ●	Создайте класс User с полями id, name, email и password.
# ●	Создайте список users для хранения пользователей.
# ●	Создайте маршрут для добавления нового пользователя (метод POST).
# ●	Реализуйте валидацию данных запроса и ответа.
import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


@app.get('/users/')
async def all_users():
    return {'users': users}


@app.post('/users/add')
async def add_users(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


if __name__ == "__main__":
    uvicorn.run("Task_3:app", port=8001)
