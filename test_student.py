import pytest
from student import Student


def test_student_creation():
    s = Student("Roaa", "123")
    assert s.name == "Roaa"
    assert s.student_id == "123"
    assert s.grades == []


def test_add_grade():
    s = Student("Ali", "001")
    s.add_grade(90)
    s.add_grade(80)
    assert s.grades == [90, 80]


def test_average():
    s = Student("Lina", "002")
    s.add_grade(100)
    s.add_grade(50)
    assert s.get_average() == 75


def test_average_empty():
    s = Student("Test", "003")
    assert s.get_average() == 0.0


def test_invalid_grade_type():
    s = Student("Test", "004")
    with pytest.raises(TypeError):
        s.add_grade("A")


def test_invalid_grade_value():
    s = Student("Test", "005")
    with pytest.raises(ValueError):
        s.add_grade(150)
