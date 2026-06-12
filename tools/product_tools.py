import json

PRODUCT_FILE = "data/products.json"


def load_products():
    with open(PRODUCT_FILE, "r") as file:
        return json.load(file)


def get_product(product_name):
    products = load_products()

    for product in products:
        if product["name"].lower() == product_name.lower():
            return product

    return None


def get_all_products():
    return load_products()