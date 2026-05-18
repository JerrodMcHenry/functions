from collections import deque

# Data structures
inventory = {}  # Dictionary / hash table for fast inventory lookup
orders = deque()  # Queue for FIFO order processing
transaction_history = []  # List for tracking activity


def add_inventory_item(sku, name, quantity):
    if not sku or not name:
        raise ValueError("SKU and name are required")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    inventory[sku] = {
        "name": name,
        "quantity": quantity
    }

    transaction_history.append(f"Added inventory item: {sku}")


def update_inventory(sku, quantity_change):
    if sku not in inventory:
        raise ValueError("SKU not found")

    if inventory[sku]["quantity"] + quantity_change < 0:
        raise ValueError("Insufficient inventory")

    inventory[sku]["quantity"] += quantity_change

    transaction_history.append(f"Updated inventory for: {sku}")


def add_order(order_id):
    if not order_id:
        raise ValueError("Order ID is required")

    orders.append(order_id)

    transaction_history.append(f"Added order: {order_id}")


def process_order():
    if not orders:
        raise ValueError("No orders to process")

    processed_order = orders.popleft()

    transaction_history.append(f"Processed order: {processed_order}")

    return processed_order


def generate_inventory_report():
    report = []

    for sku, details in inventory.items():
        report.append(
            f"{sku}: {details['name']} - Quantity: {details['quantity']}"
        )

    return report


def show_transaction_history():
    return transaction_history


# Testing section
if __name__ == "__main__":
    print("Testing Warehouse Inventory and Order Management System")
    print("-" * 60)

    # Successful inventory operations
    add_inventory_item("SKU001", "Laptop", 10)
    add_inventory_item("SKU002", "Monitor", 25)

    update_inventory("SKU001", 5)
    update_inventory("SKU002", -3)

    print("Inventory Report:")
    for item in generate_inventory_report():
        print(item)

    print("-" * 60)

    # Successful order operations
    add_order("ORDER1001")
    add_order("ORDER1002")

    print("Processed Order:")
    print(process_order())

    print("-" * 60)

    # Edge case: invalid SKU
    try:
        update_inventory("BADSKU", 5)
    except ValueError as error:
        print("Error handled:", error)

    # Edge case: insufficient inventory
    try:
        update_inventory("SKU001", -100)
    except ValueError as error:
        print("Error handled:", error)

    # Edge case: empty queue
    try:
        process_order()
        process_order()
    except ValueError as error:
        print("Error handled:", error)

    print("-" * 60)

    print("Transaction History:")
    for transaction in show_transaction_history():
        print(transaction)