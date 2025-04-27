import pytest

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


def test_smartphone_init(smartphone_1, smartphone_2):
    assert smartphone_1.name == "IPhone 15"
    assert smartphone_1.description == "Apple"
    assert smartphone_1.price == 70000
    assert smartphone_1.quantity == 200
    assert smartphone_1.efficiency == 3000
    assert smartphone_1.model == 15
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "green"
    assert smartphone_2.name == "IPhone 14"
    assert smartphone_2.description == "Apple"
    assert smartphone_2.price == 60000
    assert smartphone_2.quantity == 200
    assert smartphone_2.efficiency == 3000
    assert smartphone_2.model == 14
    assert smartphone_2.memory == 256
    assert smartphone_2.color == "gold"


def test_lawngrass_init(lawngrass_1, lawngrass_2):
    assert lawngrass_1.name == "grass"
    assert lawngrass_1.description == "grass from China"
    assert lawngrass_1.price == 800
    assert lawngrass_1.quantity == 100
    assert lawngrass_1.country == "China"
    assert lawngrass_1.color == "green"
    assert lawngrass_1.germination_period == 5
    assert lawngrass_2.name == "grass"
    assert lawngrass_2.description == "grass from Finland"
    assert lawngrass_2.price == 1800
    assert lawngrass_2.quantity == 200
    assert lawngrass_2.country == "Finland"
    assert lawngrass_2.color == "green"
    assert lawngrass_2.germination_period == 15


def test_products_add_error(product_1, lawngrass_1):
    with pytest.raises(TypeError):
        result = product_1 + lawngrass_1


def test_products_smartphone_add_error(smartphone_1, lawngrass_1):
    with pytest.raises(TypeError):
        result = smartphone_1 + lawngrass_1


def test_products_lawngrass_add_error(lawngrass_1):
    with pytest.raises(TypeError):
        result = lawngrass_1 + 1


def test_products_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 26000000


def test_products_lawngrass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 440000


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    print(message)
    assert (
        message.out.strip()
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )
