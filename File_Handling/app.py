name = input("Enter your name:   ")
with open("user.txt", "w", encoding="utf-8") as file:
    file.write(name)

print("Name save successfully")