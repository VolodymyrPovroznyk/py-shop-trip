import math


def trip_distance(
        coordinates1: list[int],
        coordinates2: list[int]
) -> int | float:
    x1, y1 = coordinates1
    x2, y2 = coordinates2
    one_way_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return one_way_distance * 2


def fuel_costs(
        customer_location: list[int],
        shop_location: list[int],
        fuel_consumption: float,
        fuel_price: float
) -> int | float:
    distance = trip_distance(customer_location, shop_location)
    fuel_used = distance * fuel_consumption / 100
    return fuel_used * fuel_price
