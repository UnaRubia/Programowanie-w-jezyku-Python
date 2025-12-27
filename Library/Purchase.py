from .Book import Book
from .Employee import Employee
from .Student import Student


class Purchase:
    """Represents a book purchase."""

    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        purchase_date: str,
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.purchase_date = purchase_date

    def __str__(self) -> str:
        books_list = "\n".join(str(book) for book in self.books)
        return (
            f"Purchase date: {self.purchase_date}\n"
            f"{self.student}\n"
            f"Handled by: {self.employee}\n"
            f"Books:\n{books_list}"
        )
