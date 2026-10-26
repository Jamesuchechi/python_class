
students = {}


def validate_name(name):
    """Check that the student's name is not empty."""
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    return name.strip()


def validate_age(age_input):
    """Ensure age is a positive integer."""
    try:
        age = int(age_input)
    except ValueError:
        raise ValueError("Age must be a whole number.")

    if age <= 0:
        raise ValueError("Age must be a positive integer.")

    return age


def register_student(student_id, name, age_input):
    """Register a student without overwriting existing records."""
    student_id = student_id.strip()

    if not student_id:
        return False, "Student ID cannot be empty."

    if student_id in students:
        return False, f"Student ID '{student_id}' already exists."

    try:
        name = validate_name(name)
        age = validate_age(age_input)
    except ValueError as error:
        return False, str(error)

    students[student_id] = {
        "name": name,
        "age": age
    }

    return True, f"Student '{name}' registered successfully!"


def display_students():
    """Display all registered students."""
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n--- Registered Students ---")

    for student_id, details in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print("-" * 25)


def main():
    """Run the command-line registration menu."""
    while True:
        print("\n=== Training Academy ===")
        print("1. Register student")
        print("2. View students")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")

            success, message = register_student(
                student_id, name, age
            )
            print(message)

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
