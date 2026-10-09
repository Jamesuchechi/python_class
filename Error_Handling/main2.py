try:
    number = int(input("Enter annumber:"))
    result = 100/ number
    print(result)
except Exception as error:
    print(f"operation error: {error}")