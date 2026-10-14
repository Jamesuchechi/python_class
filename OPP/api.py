from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserModel(BaseModel):
    name: str
    age: int

@pp.post("/user")
def create_user(user: UserModel):
    return {
        "message": "User registered successfully",
        "name": user.anme,
        "age": user.age
    }