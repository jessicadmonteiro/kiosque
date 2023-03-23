from menu import products


def calculate_tab(list_order):
    sum = 0
    for product in list_order:
        id_order = product["_id"]
        quantity = product["amount"]
        for list_product in products:
            id_product = list_product["_id"]
            if id_order == id_product:
                values = list_product["price"]
        multiplication = values * quantity
        sum += multiplication
        value = round(sum, 2)
    subtotal: dict = {"subtotal": str(f"${value}")}
    return subtotal
