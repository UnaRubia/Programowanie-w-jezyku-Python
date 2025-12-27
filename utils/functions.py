"""Utility functions for unit testing tasks."""

import re
import unicodedata
from collections import Counter
from typing import Any, Dict, List


def is_palindrome(text: str) -> bool:
    """
    Check if the given text is a palindrome.

    Ignores case and non-alphanumeric characters.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


def count_vowels(text: str) -> int:
    """
    Count vowels in the given text.

    Supports Polish characters by normalizing Unicode accents.
    """
    vowels = "aeiouy"
    normalized = unicodedata.normalize("NFD", text.lower())
    normalized = "".join(
        char
        for char in normalized
        if unicodedata.category(char) != "Mn"
    )

    return sum(1 for char in normalized if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    """
    Return price after applying a discount.

    Raises:
        ValueError: If discount is not between 0 and 1.
    """
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")

    return price * (1 - discount)


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list into a single-level list."""
    flattened: List[Any] = []

    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)

    return flattened


def word_frequencies(text: str) -> Dict[str, int]:
    """
    Return a dictionary with word frequency counts.

    Ignores case and punctuation.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))


def is_prime(n: int) -> bool:
    """Check whether a number is prime."""
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False

    return True