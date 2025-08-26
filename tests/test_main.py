import json
import os
import tempfile

from src.main import from_json, created_from_json


def test_product_init(products):
    product1, product2, product3 = products

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category.products) == 3
    assert category.category_count == 1
    assert category.product_count == 3


def test_from_json():
    test_data = {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ],
}
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.json') as temp_file:
        json.dump(test_data, temp_file, ensure_ascii=False, indent=4)
        full_path = temp_file.name
    data_file = from_json(full_path)
    assert data_file == test_data
    os.remove(full_path)

def test_created_from_json():
    test_data = {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ]
    }
    category_list = created_from_json([test_data])
    assert len(category_list) == 1
    assert category_list[0].name == "Смартфоны"




