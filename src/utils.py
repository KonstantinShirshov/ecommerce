import json
import os

from src.categories import Category
from src.products import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def creat_objects_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     raw_data = read_json('../data/products.json')
#     categories_data = creat_objects_from_json(raw_data)
#     print(categories_data[1].name)
#     print(categories_data[1].products)
