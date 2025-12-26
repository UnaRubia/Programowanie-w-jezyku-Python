#Task8


import argparse
from typing import List, Optional

import requests


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        state: str,
        country: str,
        website_url: Optional[str],
    ) -> None:
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"Brewery:\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  City: {self.city}\n"
            f"  State: {self.state}\n"
            f"  Country: {self.country}\n"
            f"  Website: {self.website_url or 'N/A'}\n"
        )


def fetch_breweries(city: Optional[str] = None) -> List[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}

    if city:
        params["by_city"] = city

    response = requests.get(url, params=params)
    response.raise_for_status()

    breweries_data = response.json()
    breweries = []

    for brewery in breweries_data:
        breweries.append(
            Brewery(
                brewery_id=brewery["id"],
                name=brewery["name"],
                brewery_type=brewery["brewery_type"],
                city=brewery["city"],
                state=brewery["state"],
                country=brewery["country"],
                website_url=brewery.get("website_url"),
            )
        )

    return breweries


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch breweries from OpenBreweryDB API"
    )
    parser.add_argument(
        "--city",
        type=str,
        help="Filter breweries by city (e.g. Berlin)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    breweries = fetch_breweries(city=args.city)

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
