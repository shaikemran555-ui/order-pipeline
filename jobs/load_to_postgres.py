import csv
import os
import psycopg2

CSV_PATH = os.environ.get("VALID_CSV", "/app/output/valid_orders.csv")

conn = psycopg2.connect(
    host=os.environ.get("PG_HOST", "localhost"),
    dbname=os.environ.get("PG_DB", "ordersdb"),
    user=os.environ.get("PG_USER", "postgres"),
    password=os.environ.get("PG_PASSWORD", "orders123"),
)

with open(CSV_PATH, newline="") as f:
    rows = list(csv.DictReader(f))

cur = conn.cursor()
for r in rows:
    cur.execute(
        """
        INSERT INTO valid_orders (order_id, customer, amount, order_date)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING
        """,
        (r["order_id"], r["customer"], r["amount"], r["order_date"]),
    )

conn.commit()
cur.close()
conn.close()
print(f"Loaded {len(rows)} rows into valid_orders")
