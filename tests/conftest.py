import pytest

from src.categories import Category
from src.products import LawnGrass, Product, Smartphone


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
def category_with_zero_price():
    return Category(
        name='Телевизоры',
        description='Современный телевизор,\
     который позволяет наслаждаться просмотром,\
     станет вашим другом и помощником')


@pytest.fixture
def product_1():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_2():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def dict_of_products1():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def smartphone_1():
    return Smartphone("IPhone 15", "Apple", 70000, 200, 3000, 15, 256, "green")


@pytest.fixture
def smartphone_2():
    return Smartphone("IPhone 14", "Apple", 60000, 200, 3000, 14, 256, "gold")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("grass", "grass from China", 800, 100, "China", 5, "green")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("grass", "grass from Finland", 1800, 200, "Finland", 15, "green")
