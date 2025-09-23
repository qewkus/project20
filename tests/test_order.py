from src.order import Order
from src.product import Product


def test_order_init(product: Product) -> None:
    """Тестируем инициализацию заказа"""
    order = Order(product, 2)
    assert order.product.name == "Samsung Galaxy S23 Ultra"
    assert order.quantity == 2
    assert order.total_price == 360000


def test_order_str(product: Product) -> None:
    """Тестируем строковое отображение заказа"""
    order = Order(product, 2)
    assert str(order) == (
        'Заказан товар "Samsung Galaxy S23 Ultra" в количестве 2 шт.\n' "Сумма к оплате 360000.00 руб."
    )
