try:
    age = int(input("Enter your age:"))
    print(f"You are {age} years old.")
except ValueError:
    print("invalid input. Please enter a whole number")