from .Library import Library


class Book:
    """Represents a book."""

    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Book by {self.author_name} {self.author_surname}, "
            f"published: {self.publication_date}, "
            f"pages: {self.number_of_pages}\n"
            f"Available in: {self.library}"
        )
