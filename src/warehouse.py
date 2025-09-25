from abc import ABC, abstractmethod


class WareHouse(ABC):
    """
    Абстрактный класс, который станет родительским для классов «Заказ» и «Категория»
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод вывода информации
        """
        pass
