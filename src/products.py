class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, dict_of_product: dict):
        from src.utils import create_objects_from_json, read_json

        raw_data = read_json("../ecommerce/data/products.json")
        categories_data = create_objects_from_json(raw_data)
        for product in categories_data[0].products_list:
            if dict_of_product["name"] == product.name:
                quantity = dict_of_product["quantity"] + product.quantity
                product.quantity = quantity
                max_price = max(dict_of_product["price"], product.__price)
                product.__price = max_price
                product.name = dict_of_product["name"]
                product.description = dict_of_product["description"]
                break
            else:
                product.name = dict_of_product["name"]
                product.description = dict_of_product["description"]
                product.__price = dict_of_product["price"]
                product.quantity = dict_of_product["quantity"]
        return Product(
            product.name, product.description, product.__price, product.quantity
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
