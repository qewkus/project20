from typing import Any, List

from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для хранения товаров"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор для товара"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        """Метод, который возвращает строку в следующем виде:
        *Название продукта, 80 руб. Остаток: 15 шт.*"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Метод для получения полной стоимости всех выбранных товаров на складе"""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict, products_list: List["Product"]) -> Any:
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает
        созданный объект класса Product"""
        try:
            if product_dict["quantity"] == 0:
                raise ZeroQuantityProduct("Попытка добавить товар с нулевым количеством")
        except ZeroQuantityProduct as e:
            print(str(e))
        else:
            for product in products_list:
                if product.name == product_dict["name"]:
                    product.quantity += product_dict["quantity"]
                    if product_dict["price"] > product.price:
                        product.price = product_dict["price"]
                    return product
            name = product_dict["name"]
            description = product_dict["description"]
            price = product_dict["price"]
            quantity = product_dict["quantity"]
            print("Товар добавлен успешно")
            return cls(name, description, price, quantity)
        finally:
            print("Обработка добавления товара завершена")

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            print(f"Цена не была изменена, она осталась {self.__price}")
            return
        else:
            if new_price < self.__price:
                print("Вы действительно хотите изменить цену на меньшую? (y/n)")
                users_choice = str(input().strip().lower())
                if users_choice == "y":
                    self.__price = new_price
                    print(f"Цена изменена на {new_price}")
                else:
                    print(f"Цена не была изменена, она осталась {self.__price}")
                    return
            else:
                self.__price = new_price
                print(f"Цена изменена на {new_price}")
