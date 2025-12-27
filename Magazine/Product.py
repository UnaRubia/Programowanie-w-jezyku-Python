"""Product module."""

from . import utils


class Product:
    """Represents a product in the magazine."""

    def __init__(self, name: str, price: float) -> None:
        self.name = utils.format_name(name)
        self.price = price

    def price_with_tax(self) -> float:
        """Return price including tax."""
        return self.price + utils.calculate_tax(self.price)

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price:.2f}"