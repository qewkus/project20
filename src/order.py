from src.main_16_2 import Product
from src.warehouse import WareHouse


class Order(WareHouse):
    """
    Класс «Заказ»
    """

    def __init__(self, product: Product, quantity: int):
        """
        Конструктор заказа
        """
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        """
        Метод вывода на печать информации о заказе и его итоговой стоимости
        """
        return (
            f'Заказан товар "{self.product.name}" в количестве {self.quantity} шт.\n'
            f"Сумма к оплате {self.total_price:.2f} руб."
        )
