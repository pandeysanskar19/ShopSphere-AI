import json
import uuid

ORDER_FILE = "data/orders.json"


def load_orders():
    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def save_orders(orders):
    with open(ORDER_FILE, "w") as file:
        json.dump(orders, file, indent=4)


def create_order(product_name, quantity=1):

    orders = load_orders()

    order = {
        "order_id": str(uuid.uuid4())[:8],
        "product": product_name,
        "quantity": quantity,
        "status": "Confirmed"
    }

    orders.append(order)

    save_orders(orders)

    return order


def get_orders():
    return load_orders()