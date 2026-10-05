users = []


def create_user(name: str, age: int) -> dict:
    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }

    users.append(user)

    return user

user1 = create_user("James", 28)
user2 = create_user("John", 25)
user3 = create_user("Jane", 67)
print(user1)
print(user2)
print(user3)
print(users)


def get_user(user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return None

user = get_user(8)
print(user)