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