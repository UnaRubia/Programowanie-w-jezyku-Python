"""Main module to run Magazine and Library examples."""

from Magazine.Product import Product
from Magazine.Order import Order as MagazineOrder

from Library.Library import Library
from Library.Employee import Employee
from Library.Student import Student
from Library.Book import Book
from Library.Purchase import Purchase


def main() -> None:
    # === MAGAZINE ===
    product_1 = Product("apple", 1.5)
    product_2 = Product("banana", 2.0)

    magazine_order = MagazineOrder()
    magazine_order.add_product(product_1)
    magazine_order.add_product(product_2)

    print("MAGAZINE ORDER")
    print(magazine_order)
    print(f"Total price with tax: {magazine_order.total_price():.2f}")
    print()

    # === LIBRARY ===
    library = Library(
        "Warsaw",
        "Main Street 1",
        "00-001",
        "8:00–18:00",
        "123-456-789",
    )

    employee = Employee(
        "Anna",
        "Nowak",
        "2020-01-10",
        "1990-05-15",
        "111-222-333",
    )

    student = Student("Lilianna", "Nowak", "S001")

    book_1 = Book(library, "2015", "George", "Orwell", 328)
    book_2 = Book(library, "2001", "J.K.", "Rowling", 400)

    purchase = Purchase(
        employee,
        student,
        [book_1, book_2],
        "2024-01-10",
    )

    print("LIBRARY PURCHASE")
    print(purchase)


if __name__ == "__main__":
    main()