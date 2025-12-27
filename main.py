"""Main module to run the magazine application."""

from Magazine import Product, Order


def main() -> None:
    """Example usage of Product and Order modules."""
    product1 = Product.Product("apple", 1.5)
    product2 = Product.Product("banana", 2.0)

    order = Order.Order()
    order.add_product(product1)
    order.add_product(product2)

    print(order)
    print(f"Total price with tax: {order.total_price():.2f}")


if __name__ == "__main__":
    main()