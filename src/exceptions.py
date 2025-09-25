from typing import Optional


class ZeroQuantityProduct(Exception):
    """Класс ошибки при нулевом количестве товара"""

    def __init__(self, message: Optional[str] = None):
        super().__init__(message)
