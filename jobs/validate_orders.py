import csv
import os
import sys

INPUT_PATH = os.environ.get("INPUT_PATH", "/app/data/orders.csv")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/app/output")


def validate_order(order):
    """Reject orders with a non-positive amount."""
    if float(order["amount"]) <= 0:
        raise ValueError(f"Non-positive amount: {order['order_id']}")
    return order


def run():
    with open(INPUT_PATH, newline="") as f:
        rows = list(csv.DictReader(f))

    valid, rejected = [], []
    for row in rows:
        try:
            valid.append(validate_order(row))
        except ValueError as e:
            row["reason"] = str(e)
            rejected.append(row)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(f"{OUTPUT_DIR}/valid_orders.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["order_id", "customer", "amount", "order_date"])
        w.writeheader()
        w.writerows(valid)

    with open(f"{OUTPUT_DIR}/rejected_orders.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["order_id", "customer", "amount", "order_date", "reason"])
        w.writeheader()
        w.writerows(rejected)

    print(f"Read {len(rows)} rows -> {len(valid)} valid, {len(rejected)} rejected")
    return 0


if __name__ == "__main__":
    sys.exit(run())
