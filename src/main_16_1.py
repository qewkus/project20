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


# if __name__ == "__main__":
#     smartphone1 = Smartphone(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
#     )
#     smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
#     smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
#
#     print(smartphone1.name)
#     print(smartphone1.description)
#     print(smartphone1.price)
#     print(smartphone1.quantity)
#     print(smartphone1.efficiency)
#     print(smartphone1.model)
#     print(smartphone1.memory)
#     print(smartphone1.color)
#
#     print(smartphone2.name)
#     print(smartphone2.description)
#     print(smartphone2.price)
#     print(smartphone2.quantity)
#     print(smartphone2.efficiency)
#     print(smartphone2.model)
#     print(smartphone2.memory)
#     print(smartphone2.color)
#
#     print(smartphone3.name)
#     print(smartphone3.description)
#     print(smartphone3.price)
#     print(smartphone3.quantity)
#     print(smartphone3.efficiency)
#     print(smartphone3.model)
#     print(smartphone3.memory)
#     print(smartphone3.color)
#
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)
#     print(grass1.color)
#
#     print(grass2.name)
#     print(grass2.description)
#     print(grass2.price)
#     print(grass2.quantity)
#     print(grass2.country)
#     print(grass2.germination_period)
#     print(grass2.color)
#
#     smartphone_sum = smartphone1 + smartphone2
#     print(smartphone_sum)
#
#     grass_sum = grass1 + grass2
#     print(grass_sum)
#
#     try:
#         invalid_sum = smartphone1 + grass1
#     except TypeError:
#         print("Возникла ошибка TypeError при попытке сложения")
#     else:
#         print("Не возникла ошибка TypeError при попытке сложения")
#
#     category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
#     category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
#
#     category_smartphones.add_product(smartphone3)
#
#     print(category_smartphones.products)
#
#     print(Category.product_count)
#
#     try:
#         category_smartphones.add_product("Not a product")
#     except TypeError:
#         print("Возникла ошибка TypeError при добавлении не продукта")
#     else:
#         print("Не возникла ошибка TypeError при добавлении не продукта")
