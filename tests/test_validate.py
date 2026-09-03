import pytest
from jobs.validate_orders import validate_order


def test_rejects_negative_amount():
    with pytest.raises(ValueError):
        validate_order({"order_id": "A1", "amount": -50})


def test_accepts_positive_amount():
    order = {"order_id": "A2", "amount": 25}
    assert validate_order(order) == order
