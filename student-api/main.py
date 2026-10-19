from fastapi import FastAPI
from config import APP_NAME

app = FastAPI(title=APP_NAME)

students: list[dict[str, str | int]] = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com", "age": 20},
    {"id": 2, "name": "Jane Smith", "email": "Janesmith@example.com", "age": 22},
    {"id": 3, "name": "Alice Johnson", "email": "alicejohnson@example.com", "age": 19},
    {"id": 4, "name": "Bob Brown", "email": "bobbrown@example.com", "age": 21}
]

@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to studnet API"}

@app.get("/students")
def get_students() -> list[dict[str, str | int]]:
    return students

@app.get("/students/{student_id}")
def get_student(
  student_id: int,
) -> dict[str, str | int] | None:
    for student in students:
        if student["id"] == student_id:
            return student
    return None