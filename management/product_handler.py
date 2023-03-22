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


def add_product(menu, **kwargs):
    listId = []
    for product in products:
        idProducts = product["_id"]
        listId.append(idProducts)
        order = sorted(listId)
        id = order[-1] + 1
    if menu == []:
        id = 1
    kwargs["_id"] = id
    menu.append(kwargs)
    return kwargs
