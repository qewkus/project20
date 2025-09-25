from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_init(product: Product) -> None:
    """Тестируем инициализацию объекта класса Product"""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_new_product_different(capsys: CaptureFixture[str], first_category: Category) -> None:
    """Тестируем метод, который принимает на вход параметры отличного от других наименований товара и возвращает
    созданный объект класса Product"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S32 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 5,
        },
        first_category.products_list,
    )
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-3] == "Товар добавлен успешно"
    assert message.out.strip().split("\n")[-2] == (
        "Product (Samsung Galaxy S32 Ultra, 256GB, Серый цвет, 200MP камера," " 180010.0, 5)"
    )
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
    assert new_product.name == "Samsung Galaxy S32 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180010.0
    assert new_product.quantity == 5


def test_product_new_product_identical(capsys: CaptureFixture[str], first_category: Category) -> None:
    """Тестируем метод, который принимает на вход параметры схожего по наименованию товара и возвращает
    измененный объект класса Product"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 5,
        },
        first_category.products_list,
    )
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Цена изменена на 180010.0"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180010.0
    assert new_product.quantity == 10


def test_product_price_setter_invalid(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если новая цена равна или ниже нуля"""
    product.price = -800
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert f"Цена не была изменена, она осталась {product.price}" in captured.out
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert f"Цена не была изменена, она осталась {product.price}"


def test_product_price_setter_yes(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если цена товара понижается при
    согласии понизить цену"""
    new_price = 800
    with patch("builtins.input", side_effect=["Y"]):
        product.price = new_price
        captured = capsys.readouterr()
        assert "Вы действительно хотите изменить цену на меньшую? (y/n)" in captured.out
        assert f"Цена изменена на {new_price}" in captured.out
        assert product.price == 800


def test_product_price_setter_no(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если цена товара понижается при
    несогласии понизить цену"""
    new_price = 800
    with patch("builtins.input", side_effect=["N"]):
        product.price = new_price
        captured = capsys.readouterr()
        assert "Вы действительно хотите изменить цену на меньшую? (y/n)" in captured.out
        assert f"Цена не была изменена, она осталась {product.price}" in captured.out
        assert product.price == 180000.0


def test_product_str(product: Product) -> None:
    """Тестируем строковое отображение продукта"""
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product: Product, other_product: Product) -> None:
    """Тестируем метод получения полной стоимости всех выбранных товаров на складе"""
    assert product + other_product == 2580000


def test_product_add_invalid(product_smartphone1: Smartphone, product_grass1: LawnGrass) -> None:
    """Тестируем поведение метода получения полной стоимости всех выбранных товаров при попытке сложить
    товары из разной категории - вызываем ошибку"""
    with pytest.raises(TypeError):
        product_smartphone1 + product_grass1


def test_product_init_invalid() -> None:
    """Тестируем поведение конструктора при попытке добавить товар разного класса с нулевым количеством, то есть
    вызываем исключение ValueError"""
    with pytest.raises(ValueError) as e1:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        assert str(e1.value) == "Товар с нулевым количеством не может быть добавлен"
    with pytest.raises(ValueError) as e2:
        Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 0, 98.2, "15", 512, "Gray space")
        assert str(e2.value) == "Товар с нулевым количеством не может быть добавлен"
    with pytest.raises(ValueError) as e3:
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 0, "США", "5 дней", "Темно-зеленый")
        assert str(e3.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_new_product_invalid(capsys: CaptureFixture[str], first_category: Category) -> None:
    """Тестируем метод new_product, когда он принимает на вход товар с нулевым количеством - вызываем исключение"""
    Product.new_product(
        {
            "name": "Samsung Galaxy S32 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 0,
        },
        first_category.products_list,
    )
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Попытка добавить товар с нулевым количеством"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
