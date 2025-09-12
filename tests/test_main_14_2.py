from typing import Any, List

import pytest

from src.main_14_2 import Category, Product


def test_product_init(products: List[Any]) -> None:
    product1, product2, product3 = products

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product() -> None:
    product_data = {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}

    product4 = Product.new_product(product_data)
    assert product4.name == '55" QLED 4K'
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7


def test_getter_price(product_data: Product) -> None:
    assert product_data.price == 123000.0


def test_setter_price(product_data: Product) -> None:
    product_data.price = 100000.0
    assert product_data.price == 100000.0


def test_setter_decreased_price(product_data: Any) -> None:
    with pytest.raises(ValueError, match="Цена должна быть положительной и больше нуля"):
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", -123000.0, 5)


def test_category_init(category: Any) -> None:
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("iPhone 14", "128GB, Чёрный", 999.99, 10)
    product2 = Product("Samsung Galaxy S23", "256GB, Белый", 899.99, 15)
    product3 = Product("Google Pixel 7", "128GB, Синий", 799.99, 20)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 3
    assert category.category_count == 1
    assert category.product_count == 3


def test_add_product() -> None:
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    assert category1.product_count == 2
    product3 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1.add_product(product3)
    assert category1.product_count == 3
    assert product3 in category1._Category__products
