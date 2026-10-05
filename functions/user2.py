def create_user(id: int, name: str, age: int) -> dict:
    user = {
        "id": 1,
        "name": name,
        "age": age
    }
    return user
user = create_user(1,"John", 78)
print(user)
print(user["name"])

