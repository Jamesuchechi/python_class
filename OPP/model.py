class UserModel:
    def __init__(self, id, name, email, is_actiave=True):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_actiave

user = UserModel(
    1,
    "John Doe",
    "johnbosco@gmail.com"
)

inactive_user = UserModel(
    2,
    "Ann Lang",
    "annalikesit@example.com",
    False
)

print(user.id)
print(user.name)
print(user.email)
print(user.is_active)

print(inactive_user.id)
print(inactive_user.name)
print(inactive_user.email)
print(inactive_user.is_active)