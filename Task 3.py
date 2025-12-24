from typing import Union


class Property:
    """Reprezentuje nieruchomość."""

    def __init__(self, area: float, rooms: int, price: float, address: str) -> None:
        self.area: float = area
        self.rooms: int = rooms
        self.price: float = price
        self.address: str = address

    def __str__(self) -> str:
        return (
            f"Property at {self.address}, area: {self.area} m², "
            f"rooms: {self.rooms}, price: {self.price} PLN"
        )


class House(Property):
    """Reprezentuje dom, dziedzicząc po Property."""

    def __init__(self, area: float, rooms: int, price: float, address: str, plot: float) -> None:
        super().__init__(area, rooms, price, address)
        self.plot: float = plot

    def __str__(self) -> str:
        return (
            f"House at {self.address}, area: {self.area} m², "
            f"rooms: {self.rooms}, plot: {self.plot} m², price: {self.price} PLN"
        )


class Flat(Property):
    """Reprezentuje mieszkanie, dziedzicząc po Property."""

    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self) -> str:
        return (
            f"Flat at {self.address}, area: {self.area} m², "
            f"rooms: {self.rooms}, floor: {self.floor}, price: {self.price} PLN"
        )


# ==== Tworzenie obiektów ====

house_1: House = House(150, 5, 750_000, "Warsaw, Maple Street 10", 500)
flat_1: Flat = Flat(60, 3, 350_000, "Krakow, Oak Avenue 7", 2)

print(house_1)
print(flat_1)