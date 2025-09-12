from src.category_iterator import Category, Product


def test_product_count() -> None:
    product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )

    assert len(category.products) == 2, "Количество продуктов должно быть 2"


def test_add_product() -> None:
    category = Category("Смартфоны", "Описание категории")
    new_product = Product("Apple iPhone 13", "256GB, Красный", 79900.0, 10)
    category.add_product(new_product)

    assert len(category.products) == 1, "Количество продуктов должно быть 1"


def test_iterate_products() -> None:
    product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category(
        "Смартфоны",
        "Описание категории",
        [product1, product2],
    )

    product_names = [product.name for product in category]
    expected_names = ['55" QLED 4K', "Xiaomi Redmi Note 11"]

    assert product_names == expected_names, f"Ожидалось {expected_names}, но получено {product_names}"


def test_category_description() -> None:
    category = Category("Смартфоны", "Тестовое описание")

    assert category.description == "Тестовое описание", "Описание категории должно совпадать"
