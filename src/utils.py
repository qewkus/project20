import json
from typing import Any, Dict, List

from src.category import Category
from src.product import Product

# import os


def read_json(path_file: str) -> List[Dict[str, Any]]:
    # full_path = os.path.abspath(path_file)
    with open(path_file, "r", encoding="utf-8") as file:
        result_json: List[Dict[str, Any]] = json.load(file)
    return result_json


def create_objects_from_json(data: List[Dict[str, Any]]) -> list[Category]:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     products_list = read_json("../data/products.json")
#     categories_list = create_objects_from_json(products_list)
#
#     print(categories_list[0].name)
#     print(categories_list[0].products)
