from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type

if __name__ == "__main__":
    print(get_product_by_id(32))
    print(get_products_by_type("dairy"))
