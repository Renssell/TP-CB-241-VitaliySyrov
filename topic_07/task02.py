class Student:
    def __init__(self, name, age):
         self.name = name
         self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} років"

students = [
    Student("Ivan", 20),
    Student("Olena", 22),
    Student("Petro", 19),
    Student("Anna", 21)
]

sorted_students = sorted(students, key=lambda s: s.age)

for student in sorted_students:
    print(student)