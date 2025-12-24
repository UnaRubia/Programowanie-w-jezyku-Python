numbers = [23, 46, 38, 27, 54]


def count_numbers(numbers_list):
    """Zwraca nową listę, w której każdy element wejściowej listy
    został pomnożony przez 2.
    """
    result = []
    for number in numbers_list:
        result.append(number * 2)
    return result


new_list = count_numbers(numbers)
print(new_list)