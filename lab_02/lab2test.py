import pytest
import csv
from lab02 import students, addNewElement, deleteElement, updateElement, printAllList, load_csv, save_csv

def add_student(name, phone, age, group):
    addNewElement(name, phone, age, group)

@pytest.fixture(autouse=True)
def clear_students():
    students.clear()
    yield
    students.clear()

def test_add_student():
    add_student("Ivan", "123", "18", "CB-241")
    assert len(students) == 1
    assert students[0]["name"] == "Ivan"

def test_delete_student():
    add_student("Oleg", "555", "20", "CB-241")
    result = deleteElement("Oleg")
    assert result is True
    assert len(students) == 0

    result = deleteElement("Noname")
    assert result is False

def test_update_student():
    add_student("Taras", "777", "19", "CB-241")

    result = updateElement("Taras", new_age="20", new_group="CB-242")
    assert result is True
    assert students[0]["age"] == "20"
    assert students[0]["group"] == "CB-242"

    result = updateElement("Noname", new_age="30")
    assert result is False

def test_print_all_list(capsys):
    add_student("Anna", "888", "21", "CB-250")
    printAllList()
    captured = capsys.readouterr()
    assert "Anna" in captured.out
    assert "888" in captured.out
    assert "21" in captured.out
    assert "CB-250" in captured.out

def test_save_and_load_csv(tmp_path):
    add_student("Ivan", "123", "18", "CB-241")
    file = tmp_path / "test.csv"
    
    save_csv(file)  
    students.clear()
    assert len(students) == 0

    load_csv(file)  
    assert len(students) == 1
    assert students[0]["name"] == "Ivan"
    assert students[0]["phone"] == "123"
    assert students[0]["age"] == "18"
    assert students[0]["group"] == "CB-241"
