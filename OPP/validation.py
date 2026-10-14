from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    age: int
    email: str

user = UserModel(name="Ada", age= 16, email="ada@example.com")
print(user.name)
print(user.age)
print(user.email)
print(user.model_dump())