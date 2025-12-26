import re
import string


def is_palindrome(text: str) -> bool:
    """Check if the given text is a palindrome (ignoring spaces and case)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("n must be >= 0")

    if n in (0, 1):
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def count_vowels(text: str) -> int:
    """Count vowels in the given text."""
    vowels = set("aeiouyąęó")
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    """Calculate price after applying a discount."""
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    """Flatten a nested list."""
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def word_frequencies(text: str) -> dict:
    """Return word frequency dictionary for the given text."""
    text = text.lower()
    text = re.sub(rf"[{string.punctuation}]", "", text)
    words = text.split()

    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

