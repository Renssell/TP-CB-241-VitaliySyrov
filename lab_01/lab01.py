
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "age":"17", "group":"CB-242"},
    {"name":"Emma", "phone":"0631234567", "age":"19", "group":"CB-241"},
    {"name":"Jon",  "phone":"0631234567", "age":"18", "group":"CB-241"},
    {"name":"Zak",  "phone":"0631234567", "age":"21", "group":"CB-242"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is " +elem["age"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter age of student: ")
    group = input("Please enter the group of student: ")
    newItem = {"name": name, "phone": phone, "age":age, "group":group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    found = False
    for item in list:
        if item["name"]==name:
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
            print(f"Student was update")
            found = True
            break
    if not found:
        print(f"Element wasn`t found")
        return
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i]["name"] > list[j]["name"]:
                list[i], list[j] = list[j], list[i]
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()