class StudentList:
    def __init__(self):
        self.students = []

    def printAllList(self):
        for s in self.students:
            print(s)

    def addNewElement(self, student):
        insertPosition = 0
        for item in self.students:
            if student.name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
        print("New element has been added")

    def deleteElement(self, name: str) -> bool:
        for i, s in enumerate(self.students):
            if s.name == name:
                del self.students[i]
                return True
        return False

    def updateElement(self, name: str, new_name=None, new_phone=None, new_age=None, new_group=None) -> bool:
        for i, item in enumerate(self.students):
            if item.name == name:
                if new_name is not None:
                    item.name = new_name
                if new_phone is not None:
                    item.phone = new_phone
                if new_age is not None:
                    item.age = new_age
                if new_group is not None:
                    item.group = new_group

                del self.students[i]
                self.addNewElement(item)
                return True

        return False

    
      

    def printAllList(self):
        for s in self.students:
            print(f"Student: {s.name}, Phone: {s.phone}, Age: {s.age}, Group: {s.group}")