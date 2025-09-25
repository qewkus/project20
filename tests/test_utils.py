from unittest.mock import MagicMock, patch

from src.product import Product
from src.utils import create_objects_from_json, read_json


@patch("json.load")
@patch("builtins.open", create=True)
def test_transactions_read(mock_open: MagicMock, mock_json: MagicMock) -> None:
    """Проверяем работу функции на открытие файла"""
    mock_json.return_value = [{"key": "value"}]
    assert read_json("test.txt") == [{"key": "value"}]
    mock_open.assert_called_once_with("test.txt", "r", encoding="utf-8")


def test_create_objects_from_json() -> None:
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство получения дополнительных функций",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            ],
        }
    ]

    categories = create_objects_from_json(test_data)
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products_in_list) == 2
    assert isinstance(categories[0].products_in_list[0], Product)
    assert categories[0].products_in_list[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products_in_list[0].description == "256GB, Серый цвет, 200MP камера"
    assert categories[0].products_in_list[0].price == 180000.0
