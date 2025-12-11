import pytest
from student import Student
from studentlist import StudentList
import tempfile
from filelog import FileUtils
import os



@pytest.fixture
def studentTest():
    " "
    return StudentList()


def test_add(studentTest):
    studentTest.addNewElement(Student("Ivan", "123", "20", "A1"))
    studentTest.addNewElement(Student("Alex", "456", "21", "A2"))
    assert [s.name for s in studentTest.students] == ["Alex", "Ivan"]


def test_update(studentTest):
    studentTest.addNewElement(Student("Ivan", "123", "20", "A1"))
    studentTest.updateElement("Ivan", new_name="Taras")
    assert studentTest.students[0].name == "Taras"

def test_delete(studentTest):
    studentTest.addNewElement(Student("Ivan", "123", "20", "A1"))
    assert studentTest.deleteElement("Ivan") is True
    assert len(studentTest.students) == 0

def test_delete_not_found(studentTest):
    assert studentTest.deleteElement("Ghost") is False

def test_student_creation():
    studentTest = Student("Ivan", "123", "18", "CB-241")
    assert studentTest.name == "Ivan"
    assert studentTest.phone == "123"
    assert studentTest.age == "18"
    assert studentTest.group == "CB-241"

def test_save_and_load_csv():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        filename = tmp.name

    try:
        studentTest = StudentList()
        studentTest.addNewElement(Student("Anna", "111", "18", "CB-241"))
        studentTest.addNewElement(Student("Oleh", "222", "19", "CB-242"))

        FileUtils.save_csv(filename, studentTest)
        studentlist_test = StudentList()
        FileUtils.load_csv(filename, studentlist_test)

        assert len(studentlist_test.students) == 2

        assert studentlist_test.students[0].name == "Anna"
        assert studentlist_test.students[1].name == "Oleh"

    finally:
        os.remove(filename)