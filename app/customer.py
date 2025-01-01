from dataclasses import dataclass

from app.shop import Shop
from app.car import fuel_costs


@dataclass
class Customer:
    name: str
    products: dict
    location: list
    money: int
    car: dict

    def total_trip_costs(self, shop: Shop, fuel_price: float) -> int | float:
        products_total_costs = shop.calculate_products_total_cost(
            self.products
        )
        fuel_total_costs = fuel_costs(
            self.location,
            shop.location,
            self.car["fuel_consumption"],
            fuel_price
        )
        return products_total_costs + fuel_total_costs
