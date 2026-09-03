CREATE TABLE IF NOT EXISTS valid_orders (
    order_id INT PRIMARY KEY,
    customer TEXT,
    amount NUMERIC(10,2),
    order_date DATE
);
