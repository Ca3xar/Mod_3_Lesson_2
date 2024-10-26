orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]




def display_orders(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")


display_orders(orders)