from typing import Any, Dict, List, Optional, Union


class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: Union[int, float], quantity: int) -> None:
        self.name = name
        self.description = description
        if price <= 0:
            raise ValueError("Цена должна быть положительной и больше нуля")
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Название продукта: {self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value

    @property
    def price(self) -> Union[int, float]:
        """Геттер для атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: Union[int, float]) -> None:
        """Сеттер для атрибута цены с проверкой на положительное значение"""
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной и больше нуля")
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Класс-метод для создания нового продукта из словаря"""
        return cls(
            name=str(product_data.get("name", "")),
            description=str(product_data.get("description", "")),
            price=product_data.get("price", 0),
            quantity=int(product_data.get("quantity", 0)),
        )


class Category:
    name: str
    description: str
    __products: List[Product] = []  # Приватный атрибут списка товаров с аннотацией типа
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        if products is None:
            products = []
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        return f"Название категории: {self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в приватный атрибут products"""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик продуктов

    @property
    def products(self) -> list[Product]:
        """Геттер для приватного атрибута products"""
        return self.__products


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
