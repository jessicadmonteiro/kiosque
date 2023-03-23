from menu import products
from collections import defaultdict


def get_product_by_id(number):
    if not type(number) is int:
        raise TypeError("product id must be an int")
    for product in products:
        id = product["_id"]
        if number == id:
            return product
    return {}


def get_products_by_type(string):
    if not type(string) is str:
        raise TypeError("product type must be a str")
    list_products = []
    for product in products:
        type_product = product["type"]
        if string == type_product:
            list_products.append(product)
    return list_products


def add_product(menu, **kwargs):
    list_id = []
    for product in products:
        id_products = product["_id"]
        list_id.append(id_products)
        order = sorted(list_id)
        id = order[-1] + 1
    if menu == []:
        id = 1
    kwargs["_id"] = id
    menu.append(kwargs)
    return kwargs


def menu_report():
    sum = 0
    keys = defaultdict(list)
    list_type_product = []
    list_values = []
    product_count = len(products)
    for product in products:
        price_product = product["price"]
        sum += price_product / product_count
        average_price = round(sum, 2)
        type_product = product["type"]
        list_type_product.append(type_product)
        for key, value in enumerate(list_type_product):
            keys[value].append(key)
        for value in keys:
            if len(keys[value]) > 1:
                len_type = value, len(keys[value])
                list_values.append(len_type[1])
                list_values.sort()
                if len_type[1] == list_values[-1]:
                    most_common_type = len_type[0]
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
