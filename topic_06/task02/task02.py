import csv

studentList = []

with open("book.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        studentList.append({"name":row["StudentName"],
                            "mark":row["StudentMark"]})

def getName(student):
    return student["name"]

def getMark(student):
    return student["mark"]

for elem in sorted(studentList, key=lambda student: student["mark"]):
   print(f"Name = {elem['name']}  mark = {elem['mark']}")