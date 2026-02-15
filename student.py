class Student:
    school_name = "Default University"  # class variable

    def __init__(self, name: str, student_id: str):
        self.name = name                  # instance variable
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade: float):
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")

        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return (
            f"Student(name={self.name}, "
            f"id={self.student_id}, "
            f"average={self.get_average():.2f})"
        )

    def __repr__(self):
        return (
            f"Student(name='{self.name}', "
            f"student_id='{self.student_id}', "
            f"grades={self.grades})"
        )
