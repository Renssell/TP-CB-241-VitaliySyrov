from lab02 import students, addNewElement, deleteElement, updateElement, printAllList

def add_student_direct(name, phone, age, group):
    students.append({"name": name, "phone": phone, "age": age, "group": group})


def test_add_student():
    students.clear()
    add_student_direct("Ivan", "123", "18", "CB-241")

    assert len(students) == 1
    assert students[0]["name"] == "Ivan"
    assert students[0]["phone"] == "123"
    assert students[0]["age"] == "18"
    assert students[0]["group"] == "CB-241"


def test_delete_student():
    students.clear()
    add_student_direct("Oleg", "555", "20", "CB-241")
    assert len(students) == 1

    del students[0]

    assert len(students) == 0


def test_update_student():
    students.clear()
    add_student_direct("Taras", "777", "19", "CB-241")

    students[0]["age"] = "20"
    students[0]["group"] = "CB-242"

    assert students[0]["age"] == "20"
    assert students[0]["group"] == "CB-242"


def test_print_all_list(capsys):
    students.clear()
    add_student_direct("Anna", "888", "21", "CB-250")

    printAllList()
    captured = capsys.readouterr()

    assert "Anna" in captured.out
    assert "888" in captured.out
    assert "21" in captured.out
    assert "CB-250" in captured.out
