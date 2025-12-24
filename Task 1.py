class Student:
    """Reprezentuje studenta z listą ocen."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        """Zwraca True, jeśli średnia ocen jest większa niż 50."""
        average = sum(self.marks) / len(self.marks)
        return average > 50


# Przykładowe obiekty
student_passed = Student("Lilianna", [60, 70, 80])
student_failed = Student("Mateusz", [30, 40, 45])

print(student_passed.is_passed())
print(student_failed.is_passed())