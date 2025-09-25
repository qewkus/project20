from src.lawngrass import LawnGrass


def test_LawnGrass_init(product_grass1: LawnGrass) -> None:
    """Тестируем инициализацию объекта класса LawnGrass"""
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"
