numbers = list(range(27, 37))


def show_second(numbers_list):
    """Wyświetla co drugi element z przekazanej listy."""
    for number in numbers_list[::2]:
        print(number)


show_second(numbers)