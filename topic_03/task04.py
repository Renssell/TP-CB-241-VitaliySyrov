list = [
    {"name":"Bob"},
    {"name":"Emma"},
    {"name":"Jon"},
    {"name":"Zak"}
]

def addNewElement():
    name = input("Pease enter student name: ")
    newItem = {"name": name}
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

addNewElement()
print(list)