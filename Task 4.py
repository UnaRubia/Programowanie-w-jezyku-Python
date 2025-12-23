x = 2
y = 3
i = 5


def comp_numbers(a, b, c):
    """Porównuje, czy suma dwóch liczb jest równa trzeciej liczbie.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.
        c (int): Liczba do porównania z sumą a i b.

    Returns:
        bool: True jeśli suma a i b jest równa c, False w przeciwnym wypadku.
    """
    return (a + b) == c


result = comp_numbers(x, y, i)

if result:
    print(f"{x + y} is equal to {i}")
else:
    print(f"{x + y} is different from {i}")