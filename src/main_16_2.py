from typing import Any, Dict, List, Optional, Union

from src.base_product import BaseProduct


class Product(BaseProduct):
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

    def __add__(self, other: "Product") -> float:
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

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
    products_list: list = []

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        if products is None:
            products = []
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)
        Category.products_list.extend(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в приватный атрибут products"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
            Category.products_list.append(product)
        else:
            raise TypeError

    @property
    def products(self) -> List[Product]:
        """Геттер для приватного атрибута products"""
        return self.__products

    def total_quantity(self) -> int:
        """Метод для подсчета общего количества товаров в категории"""
        return sum(product.quantity for product in self.products)

    def __str__(self) -> str:
        return f"Название категории: {self.name}, количество продуктов: {self.total_quantity()} шт."


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
