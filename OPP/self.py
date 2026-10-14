class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

student1 = Student("Mike")
student2 = Student("Emma")

student1.introduce()
student2.introduce()