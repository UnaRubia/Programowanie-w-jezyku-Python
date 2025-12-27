class Employee:
    """Represents a library employee."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        phone: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.last_name}, "
            f"hired: {self.hire_date}, phone: {self.phone}"
        )
