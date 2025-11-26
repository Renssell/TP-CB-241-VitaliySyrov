import sys
import csv

students = []
def load_csv(filename):
    global students
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            students = [row for row in reader]
        print(f"Loaded {len(students)} students from CSV")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty list.")
        students = []

def save_csv(filename):
    global students
    with open(filename, "w", newline='') as csvfile:
        studentnames = ["name", "phone", "age", "group"]
        writer = csv.DictWriter(csvfile, fieldnames=studentnames)
        writer.writeheader()
        writer.writerows(students)
    print(f"Data saved to '{filename}'")

def printAllList():
    for elem in students:
        print(f"Student name is {elem['name']}, Phone is {elem['phone']}, "
              f"Age is {elem['age']}, Group is {elem['group']}")

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter age of student: ")
    group = input("Please enter the group of student: ")
    newItem = {"name": name, "phone": phone, "age":age, "group":group}
    # find insert position
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del students[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for index, newitem in enumerate(students):  
        if newitem["name"] == name:
            deletePosition = index  
            item = newitem         
            break
    if deletePosition == -1:
        print("Element was not found")
        return
    students.pop(deletePosition)
    upd = input(f"What do you wanna change? N - name, P - phone, A - age, G - group, Q - quit: ")
    match upd:
        case "N" | "n":
                    newname = input(f"Enter new name for student: ")
                    item["name"] = newname
        case "P" | "p":
                    newphone = input(f"Enter new phone for student: ")
                    item["phone"] = newphone
        case "A" | "a":
                    newage = input(f"Enter new age for student: ")
                    item["age"] = newage
        case "G" | "g":
                    newgroup = input(f"Enter new group for student: ")
                    item["group"] = newgroup
        case "Q" | "q":
                    print("Update canceled")
                    return
        case _:
                    print("Wrong choice")
    insertPosition = 0
    for s in students:
        if item["name"] > s["name"]:
            insertPosition += 1
        else:
            break
        
    students.insert(insertPosition, item)
    print("Student was update")
    # implementation required

def main():
    csv_input = "lab2.csv"
    if len(sys.argv) > 1:
        csv_input = sys.argv[1]

    load_csv(csv_input)

    while True:
        choice = input("Specify action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                addNewElement()
            case "U" | "u":
                updateElement()
            case "D" | "d":
                deleteElement()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                save_csv(csv_input)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()