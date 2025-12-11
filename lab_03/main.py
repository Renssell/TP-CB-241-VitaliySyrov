from studentlist import StudentList
from student import Student
from filelog import FileUtils
import sys

def main():
    csv_input = "lab3.csv"
    if len(sys.argv) > 1:
        csv_input = sys.argv[1]

    sl = StudentList()
    FileUtils.load_csv(csv_input, sl)

    while True:
        choice = input("Specify action [C create, U update, D delete, P print, X exit]: ")

        match choice:
            case "C" | "c":
                name = input("Name: ")
                phone = input("Phone: ")
                age = input("Age: ")
                group = input("Group: ")
                sl.addNewElement(Student(name, phone, age, group))

            case "U" | "u":
                name = input("Name to update: ")

                if not any(s.name == name for s in sl.students):
                    print("Element was not found")
                    continue

                new_name = input("New name (enter to skip): ") or None
                new_phone = input("New phone (enter to skip): ") or None
                new_age = input("New age (enter to skip): ") or None
                new_group = input("New group (enter to skip): ") or None

                sl.updateElement(name, new_name, new_phone, new_age, new_group)

            case "D" | "d":
                name = input("Name to delete: ")
                if not sl.deleteElement(name):
                    print("Element was not found")

            case "P" | "p":
                sl.printAllList()

            case "X" | "x":
                FileUtils.save_csv(csv_input, sl)
                print("Exit()")
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()