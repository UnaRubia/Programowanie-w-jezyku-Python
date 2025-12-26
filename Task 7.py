import requests
from typing import List, Optional


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: str,
        state: str,
        postal_code: str,
        country: str,
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str],
    ) -> None:
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        address = (
            f"{self.street}, {self.city}, {self.state}, "
            f"{self.postal_code}, {self.country}"
            if self.street
            else f"{self.city}, {self.state}, {self.country}"
        )

        return (
            "Brewery:\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  Address: {address}\n"
            f"  Location: latitude={self.latitude}, "
            f"longitude={self.longitude}\n"
            f"  Phone: {self.phone or 'N/A'}\n"
            f"  Website: {self.website_url or 'N/A'}"
        )


def fetch_breweries(limit: int = 20) -> List[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": limit}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    breweries_data = response.json()
    breweries: List[Brewery] = []

    for item in breweries_data:
        brewery = Brewery(
            brewery_id=item["id"],
            name=item["name"],
            brewery_type=item["brewery_type"],
            street=item.get("street"),
            city=item["city"],
            state=item["state"],
            postal_code=item["postal_code"],
            country=item["country"],
            longitude=item.get("longitude"),
            latitude=item.get("latitude"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
        )
        breweries.append(brewery)

    return breweries


def main() -> None:
    breweries = fetch_breweries()

    for brewery in breweries:
        print(brewery)
        print("-" * 40)


if __name__ == "__main__":
    main()