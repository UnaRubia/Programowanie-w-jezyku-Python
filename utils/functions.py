"""Utility functions for unit testing tasks."""

import re
from typing import Any


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignore case and spaces)."""
    cleaned_text = "".join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("n must be non-negative")

    if n in (0, 1):
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def count_vowels(text: str) -> int:
    """Count vowels in a text."""
    vowels = "aeiouy"
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    """Return price after discount."""
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")

    return price * (1 - discount)


def flatten_list(nested_list: list[Any]) -> list[Any]:
    """Flatten a nested list."""
    flattened = []

    for element in nested_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)

    return flattened


def word_frequencies(text: str) -> dict[str, int]:
    """Return word frequency dictionary."""
    words = re.findall(r"\b\w+\b", text.lower())
    frequencies: dict[str, int] = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False

    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False

    return True