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

def addNewElement(name, phone, age, group):
    newItem = {
        "name": name,
        "phone": phone,
        "age": age,
        "group": group
    }
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)

def deleteElement(name):
    global students
    for i, item in enumerate(students):
        if item["name"] == name:
            del students[i]
            return True
    return False


def updateElement(name, new_name=None, new_phone=None, new_age=None, new_group=None):
    global students
    deletePosition = -1
    item = None
    for index, newitem in enumerate(students):
        if newitem["name"] == name:
            deletePosition = index
            item = newitem
            break
    if deletePosition == -1:
        return False  

    students.pop(deletePosition)

    if new_name is not None:
        item["name"] = new_name
    if new_phone is not None:
        item["phone"] = new_phone
    if new_age is not None:
        item["age"] = new_age
    if new_group is not None:
        item["group"] = new_group

    insertPosition = 0
    for s in students:
        if item["name"] > s["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, item)

    return True



def main():
    csv_input = "lab2.csv"
    if len(sys.argv) > 1:
        csv_input = sys.argv[1]

    load_csv(csv_input)

    while True:
        choice = input("Specify action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                age = input("Enter age: ")
                group = input("Enter group: ")
                addNewElement(name, phone, age, group)
            case "U" | "u":
                name = input("Name to update: ")
                if not any(s["name"] == name for s in students):
                        print("Element was not found")
                        continue
                new_name = input("New name (enter to skip): ") or None
                new_phone = input("New phone (enter to skip): ") or None
                new_age = input("New age (enter to skip): ") or None
                new_group = input("New group (enter to skip): ") or None
                updateElement(name, new_name, new_phone, new_age, new_group)            
            case "D" | "d":
                name = input("Name to delete: ")
                if deleteElement(name):
                    print(f"Deleted student {name}")
                else:
                    print("Element was not found")
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