def test_product_init(product_1, product_2):
    assert product_1.name == '55" QLED 4K'
    assert product_1.description == "Фоновая подсветка"
    assert product_1.price == 123000.0
    assert product_1.quantity == 7
    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.price == 180000.0
    assert product_2.quantity == 5
