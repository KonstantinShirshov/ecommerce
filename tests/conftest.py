import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
        products=[
            Product(
                "Samsung Galaxy C23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            )
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product_1():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_2():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
