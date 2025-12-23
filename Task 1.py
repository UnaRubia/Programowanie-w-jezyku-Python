name = "Anna"
surname = "Kowalska"


def hi_function(name: str, surname: str) -> str:
    """
    Funkcja przyjmuje imię i nazwisko,
    zwraca powitanie w formacie: 'Hi <name>, <surname>'.
    """
    return f"Hi {name}, {surname}"


new_hi_message = hi_function(name, surname)

print(new_hi_message)
