def validate_order(order):
    """Reject orders with a negative amount."""
    if order["amount"] < 0:
        raise ValueError(f"Negative amount: {order['order_id']}")
    return order
