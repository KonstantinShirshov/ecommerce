from src.products import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        products_sum = 0
        for product in self.__products:
            products_sum += product.quantity
        return f"{self.name}, количество продуктов: {products_sum} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            print(
                sum([product.price * product.quantity for product in self.__products])
            )
            print(sum([product.quantity for product in self.__products]))
            return sum(
                [product.price * product.quantity for product in self.__products]
            ) / sum([product.quantity for product in self.__products])
        except ZeroDivisionError:
            return 0
