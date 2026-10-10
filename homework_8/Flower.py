from dataclasses import dataclass


@dataclass
class Flower:
    name: str
    price: float
    life_time_in_hours: float


class Rose(Flower):
    def __init__(self, price: float, life_time_in_hours: float):
        super().__init__(name="Роза", price=price,
                         life_time_in_hours=life_time_in_hours)


class Tulip(Flower):
    def __init__(self, price: float, life_time_in_hours: float):
        super().__init__(name="Тюльпан", price=price,
                         life_time_in_hours=life_time_in_hours)


class Lily(Flower):
    def __init__(self, price: float, life_time_in_hours: float):
        super().__init__(name="Лилия", price=price,
                         life_time_in_hours=life_time_in_hours)


class Orchid(Flower):
    def __init__(self, price: float, life_time_in_hours: float):
        super().__init__(name="Орхидея", price=price,
                         life_time_in_hours=life_time_in_hours)
