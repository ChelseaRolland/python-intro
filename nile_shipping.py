from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

def calculate_shipping_cost(from_coords, to_coords, shipping_type):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    #distance = get_distance(*from_coords, *to_coords)
    #shipping_rate = SHIPPING_PRICES.get(shipping_type)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)
