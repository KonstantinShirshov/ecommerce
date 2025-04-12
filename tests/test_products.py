from src.products import Product


def test_product_init(product_1, product_2):
    assert product_1.name == '55" QLED 4K'
    assert product_1.description == "Фоновая подсветка"
    assert product_1.price == 123000.0
    assert product_1.quantity == 7
    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.price == 180000.0
    assert product_2.quantity == 5


def test_products_new_product(dict_of_products1):
    new_product1 = Product.new_product(dict_of_products1)
    assert new_product1.name == "Samsung Galaxy S23 Ultra"
    assert new_product1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product1.price == 180000
    assert new_product1.quantity == 10


def test_str_products(product_1):
    assert str(product_1) == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_add_products(product_1, product_2):
    assert product_1 + product_2 == 1761000.0
