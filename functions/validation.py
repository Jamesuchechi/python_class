def create_user(name: str, age: int, country: str = "Nigeria") -> dict:
    if age < 18:
        return {
            "error": "User must at least be 18 years old"
        }
    return {
        "name": name,
        "age": age,
        "country": country
        }
user = create_user("John", 19)
print(user)
    