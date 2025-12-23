list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 6, 8, 10]


def com_cube(list_1, list_2):
    """Łączy dwie listy, usuwa duplikaty i zwraca listę sześcianów elementów.

    Args:
        list_1 (list): Pierwsza lista liczb.
        list_2 (list): Druga lista liczb.

    Returns:
        list: Lista sześcianów unikalnych elementów połączonych list.
    """
    combined = list_1 + list_2
    unique_values = list(set(combined))
    cubed_values = [x ** 3 for x in unique_values]
    return cubed_values


result_list = com_cube(list_1, list_2)
print(result_list)