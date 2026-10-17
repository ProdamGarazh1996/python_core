from dataclasses import dataclass


@dataclass
class Accessory:
    name: str
    price: float


class KraftPaperRoll(Accessory):
    def __init__(self, price: float):
        super().__init__(name="Крафт-бумага в рулонах", price=price)


class SatinRibbon(Accessory):
    def __init__(self, price: float):
        super().__init__(name="Атласная лента", price=price)


class Felt(Accessory):
    def __init__(self, price: float):
        super().__init__(name="Фетр", price=price)
