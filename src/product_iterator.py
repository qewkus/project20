from typing import Any

from src.category import Category


class ProductIterator:
    """Класс, с помощью которого можно перебирать все товары в заданной категории"""

    def __init__(self, category_obj: "Category"):
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Метод для получения итератора для перебора"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Метод для получения следующего товара в итераторе"""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
