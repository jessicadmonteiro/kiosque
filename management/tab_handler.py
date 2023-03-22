from menu import products


def calculate_tab(listOrder):
    sum = 0
    for product in listOrder:
        idOrder = product["_id"]
        quantity = product["amount"]
        for productList in products:
            idProduct = productList["_id"]
            if idOrder == idProduct:
                values = productList["price"]
        multiplication = values * quantity
        sum += multiplication
        value = round(sum, 2)
    subtotal: dict = {"subtotal": str(f"${value}")}
    return subtotal
