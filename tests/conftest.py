from typing import List

import pytest

from src.main_14_1 import Category, Product


@pytest.fixture
def products() -> List[Product]:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [product1, product2, product3]


@pytest.fixture
def category(products: List[Product]) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=products,
    )


@pytest.fixture
def product_data() -> Product:
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)
