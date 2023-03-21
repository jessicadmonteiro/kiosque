from menu import products


def get_product_by_id(number):
    for product in products:
        id = product["_id"]
        if number == id:
            return product
    return {}


def get_products_by_type(string):
    list = []
    for product in products:
        typeProduct = product["type"]
        if string == typeProduct:
            list.append(product)
    return list
