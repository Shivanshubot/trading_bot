def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(qty: float):
    if qty <= 0:
        raise ValueError("Quantity must be positive")


def validate_price(price, order_type):
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("LIMIT orders require a valid price")