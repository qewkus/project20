from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """
    Абстрактный класс, который станет родительским для класса продуктов
    """

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass
