def create_user(name: str, age: int) -> dict:
    user = {
        "name": name,
        "age": age
    }
    return user

user = create_user("James", 28)
print(user)