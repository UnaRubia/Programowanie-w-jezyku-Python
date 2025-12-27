"""Utility functions for the magazine package."""


def calculate_tax(price: float, tax_rate: float = 0.2) -> float:
    """Calculate tax for a given price."""
    return price * tax_rate


def format_name(name: str) -> str:
    """Format product or order name."""
    return name.strip().title()
