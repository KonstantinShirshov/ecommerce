import pytest


def test_categories_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_1.category_count == 2
    assert category_2.category_count == 2
    assert category_1.product_count == 2
    assert category_2.product_count == 2


def test_categories_property(category_1, product_1):
    assert category_1.product_count == 3
    category_1.add_product(product_1)
    assert category_1.product_count == 4


def test_str_categories(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 5 шт."


def test_categories_add_product_error(category_1, category_2):
    with pytest.raises(TypeError):
        category_1.add_product(category_2)
