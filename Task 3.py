x = 6
y = 5


def is_even(number):
    """Sprawdza, czy podana liczba jest parzysta.

    Args:
        number (int): Liczba do sprawdzenia.

    Returns:
        bool: True jeśli liczba jest parzysta, False w przeciwnym wypadku.
    """
    return number % 2 == 0


result = is_even(x)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")