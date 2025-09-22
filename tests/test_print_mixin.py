from _pytest.capture import CaptureFixture

from src.main_16_2 import LawnGrass, Product, Smartphone


def test_print_mixin(capsys: CaptureFixture[str]) -> None:
    """
    Тестируем поведение класса-миксин при добавлении товаров разных классов
    """
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product (Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Smartphone (Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    captured = capsys.readouterr()
    assert captured.out.strip() == "LawnGrass (Газонная трава 2, Выносливая трава, 450.0, 15)"
