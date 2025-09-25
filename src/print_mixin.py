class PrintMixin:
    """
    Класс-миксин, который при создании объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        """
        Метод, который реализует вывод информации в консоль согласно заданному шаблону:
        *Product('Продукт1', 'Описание продукта', 1200, 10)*
        """
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
