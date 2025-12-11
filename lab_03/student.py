class Student:
    def __init__(self, name, phone, age, group):
        self.name = name
        self.phone = phone
        self.age = age
        self.group = group

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "age": self.age,
            "group": self.group
        }
