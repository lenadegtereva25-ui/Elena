import doctest

class Phone:
    """Телефон"""

    def __init__(self, brand: str, battery_level: int):
        """
        :param brand: марка телефона
        :param battery_level: уровень заряда батареи (0–100 %)
        >>> phone = Phone("Samsung", 50)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not (0 <= battery_level <= 100):
            raise ValueError("Заряд батареи должен быть от 0 до 100 %")
        self.brand = brand
        self.battery_level = battery_level

    def call(self, number: str) -> str:
        """
        Позвонить на номер.
        :param number: номер телефона
        :return: сообщение о звонке
        >>> phone = Phone("Xiaomi", 80)
        >>> phone.call("+79991234567")
        'Звонок на +79991234567'
        """
        return f"Звонок на {number}"

    def charge(self, minutes: int) -> None:
        """
        Зарядить телефон.
        :param minutes: минуты зарядки
        >>> phone = Phone("Apple", 20)
        >>> phone.charge(30)
        """
        if minutes < 0:
            raise ValueError("Время зарядки не может быть отрицательным")
        # Заглушка без логики
        pass

    def get_battery(self) -> int:
        """
        Получить текущий заряд батареи.
        :return: уровень заряда в процентах
        >>> phone = Phone("Huawei", 75)
        >>> phone.get_battery()
        75
        """
        return self.battery_level



class Cup:
    """Кружка"""

    def __init__(self, color: str, volume: int):
        """
        :param color: цвет кружки
        :param volume: объём в мл
        >>> cup = Cup("красная", 300)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if volume <= 0:
            raise ValueError("Объём должен быть положительным")
        self.color = color
        self.volume = volume

    def fill(self, amount: int) -> None:
        """
        Наполнить кружку.
        :param amount: количество жидкости в мл
        >>> cup = Cup("синяя", 250)
        >>> cup.fill(200)
        """
        if amount < 0:
            raise ValueError("Количество жидкости не может быть отрицательным")
        # Заглушка без логики
        pass

    def drink(self, sips: int) -> int:
        """
        Отпить несколько глотков.
        :param sips: количество глотков
        :return: сколько глотков сделано
        >>> cup = Cup("зелёная", 400)
        >>> cup.drink(3)
        3
        """
        if sips < 0:
            raise ValueError("Количество глотков не может быть отрицательным")
        return sips

class Door:
    """Дверь"""

    def __init__(self, material: str, is_open: bool):
        """
        :param material: материал двери
        :param is_open: открыта ли дверь (True/False)
        >>> door = Door("дерево", False)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material
        self.is_open = is_open

    def open(self) -> None:
        """
        Открыть дверь.
        >>> door = Door("металл", False)
        >>> door.open()
        """
        self.is_open = True

    def close(self) -> None:
        """
        Закрыть дверь.
        >>> door = Door("пластик", True)
        >>> door.close()
        """
        self.is_open = False

    def toggle(self) -> bool:
        """
        Переключить состояние двери (открыть/закрыть).
        :return: новое состояние (True — открыта, False — закрыта)
        >>> door = Door("стекло", False)
        >>> door.toggle()
        True
        """
        self.is_open = not self.is_open
        return self.is_open

if __name__ == "__main__":
    doctest.testmod()
