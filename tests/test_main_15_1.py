from src.main_15_1 import Category, Product


def test_product_str():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    expected_output = "Название продукта: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected_output, f"Ошибка: {str(product)} != {expected_output}"


def test_product_addition():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    total_value = product1 + product2
    expected_value = (180000 * 5) + (210000 * 8)
    assert total_value == expected_value, f"Ошибка: {total_value} != {expected_value}"


def test_product_invalid_price():
    try:
        Product("Invalid Product", "Description", -100.0, 10)
        assert False, "Ошибка: исключение не было выброшено"
    except ValueError:
        pass  # Ожидаем исключение


def test_category_creation():
    category = Category("Смартфоны", "Смартфоны категории")
    assert category.name == "Смартфоны", f"Ошибка: {category.name} != Смартфоны"
    assert category.description == "Смартфоны категории", f"Ошибка: {category.description} != Смартфоны категории"
    assert Category.category_count == 1, f"Ошибка: {Category.category_count} != 1"


def test_add_product_to_category():
    category = Category("Смартфоны", "Смартфоны категории")
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    category.add_product(product)
    assert len(category.products) == 1, f"Ошибка: {len(category.products)} != 1"
