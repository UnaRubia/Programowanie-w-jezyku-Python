numbers = list(range(27, 38))


def show_even(numbers_list):
    """Wyświetla wszystkie liczby parzyste z przekazanej listy."""
    for number in numbers_list:
        if number % 2 == 0:
            print(number)


show_even(numbers)