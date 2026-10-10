from dataclasses import dataclass
from homework_8.Accessories import Accessory
from homework_8.Flower import Flower


@dataclass
class BouquetOfFlowers:

    def __init__(self, flowers=None, accessories=None):
        if flowers is None:
            flowers = []
        if accessories is None:
            accessories = []
        self.__flowers = flowers
        self.__accessories = accessories

    def get_total_price_of_flowers(self) -> float:
        flower_sum = sum(f.price for f in self.__flowers)
        accessory_sum = sum(a.price for a in self.__accessories)
        return flower_sum + accessory_sum

    def get_average_life_time(self) -> float:
        total_sum = sum(f.life_time_in_hours for f in self.__flowers)
        return total_sum / len(self.__flowers)

    def contains_specific_flower(self, flower_name) -> bool:
        return flower_name in map(lambda f: f.name, self.__flowers)

    def sort_flowers_by_price(self) -> list[Flower]:
        return sorted(self.__flowers, key=lambda f: f.price)

    def add_flower(self, flower: Flower):
        self.__flowers.append(flower)

    def remove_flower(self, flower: Flower):
        self.__flowers.remove(flower)

    def add_accessory(self, accessory: Accessory):
        self.__accessories.append(accessory)

    def remove_accessory(self, accessory: Accessory):
        self.__accessories.remove(accessory)
