class Library:
    """Reprezentuje bibliotekę."""

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.city}, {self.street}, {self.zip_code}, "
            f"open hours: {self.open_hours}, phone: {self.phone}"
        )


class Employee:
    """Reprezentuje pracownika biblioteki."""

    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"hired: {self.hire_date}, phone: {self.phone}"
        )


class Student:
    """Reprezentuje studenta."""

    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (ID: {self.student_id})"


class Book:
    """Reprezentuje książkę."""

    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book by {self.author_name} {self.author_surname}, "
            f"published: {self.publication_date}, pages: {self.number_of_pages}\n"
            f"Available in: {self.library}"
        )


class Order:
    """Reprezentuje zamówienie książek."""

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"{self.student}\n"
            f"Handled by: {self.employee}\n"
            f"Books:\n{books_list}"
        )


# ==== Tworzenie obiektów ====

library_1 = Library(
    "Warsaw", "Main Street 1", "00-001", "8:00–18:00", "123-456-789"
)
library_2 = Library(
    "Krakow", "Library Street 5", "30-002", "9:00–17:00", "987-654-321"
)

employee_1 = Employee(
    "Anna", "Nowak", "2020-01-10", "1990-05-15",
    "Warsaw", "Green 2", "00-010", "111-222-333"
)
employee_2 = Employee(
    "Marek", "Kowalski", "2019-03-20", "1985-11-02",
    "Krakow", "Blue 5", "30-020", "222-333-444"
)
employee_3 = Employee(
    "Julia", "Wiśniewska", "2021-06-01", "1995-07-07",
    "Warsaw", "Red 9", "00-030", "333-444-555"
)

student_1 = Student("Lilianna", "Nowak", "S001")
student_2 = Student("Mateusz", "Kaczmarek", "S002")
student_3 = Student("Olga", "Zielińska", "S003")

book_1 = Book(library_1, "2015", "George", "Orwell", 328)
book_2 = Book(library_1, "2001", "J.K.", "Rowling", 400)
book_3 = Book(library_2, "2010", "Dan", "Brown", 500)
book_4 = Book(library_2, "1997", "Stephen", "King", 350)
book_5 = Book(library_1, "2020", "Yuval", "Harari", 450)

order_1 = Order(
    employee_1,
    student_1,
    [book_1, book_2],
    "2024-01-10",
)

order_2 = Order(
    employee_2,
    student_2,
    [book_3, book_4, book_5],
    "2024-01-12",
)

print(order_1)
print()
print(order_2)