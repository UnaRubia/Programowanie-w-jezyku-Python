class Student:
    """Represents a student."""

    def __init__(self, first_name: str, last_name: str, student_id: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} (ID: {self.student_id})"