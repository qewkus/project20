import pytest

from src.main_16_1 import Category, LawnGrass, Smartphone


def test_LawnGrass_init(product_grass1: LawnGrass) -> None:
    """Тестируем инициализацию объекта класса LawnGrass"""
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"


def test_product_add_invalid(product_smartphone1: Smartphone, product_grass1: LawnGrass) -> None:
    """Тестируем поведение метода получения полной стоимости всех выбранных товаров при попытке сложить
    товары из разной категории - вызываем ошибку"""
    with pytest.raises(TypeError):
        product_smartphone1 + product_grass1


def test_smartphone_init(product_smartphone1: Smartphone) -> None:
    """Тестируем инициализацию объекта класса Smartphone"""
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_product_count() -> None:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1])

    total_count = len(category_smartphones.products) + len(category_grass.products)

    assert Category.product_count == total_count
