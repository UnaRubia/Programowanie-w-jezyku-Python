"""Order module."""

from . import utils
from .Product import Product


class Order:
    """Represents an order containing multiple products."""

    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the order."""
        self.products.append(product)

    def total_price(self) -> float:
        """Calculate total price including tax."""
        return sum(product.price_with_tax() for product in self.products)

    def __str__(self) -> str:
        product_list = ', '.join([p.name for p in self.products])
        return f"Order: {product_list}, Total: {self.total_price():.2f}"