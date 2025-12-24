numbers = [23, 46, 38, 27, 54]


def count_numbers(numbers_list):
    """Zwraca nową listę, w której każdy element został pomnożony przez 2,
    używając listy składanej.
    """
    return [number * 2 for number in numbers_list]


new_list = count_numbers(numbers)
print(new_list)