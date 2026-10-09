try:
    number = int(input("Enter annumber:"))
    result = 100/ number
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or Cannot be zero")

try:
    resu = 10 / 0
except:
    print("something went wrong")