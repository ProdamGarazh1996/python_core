from homework_8.Accessories import KraftPaperRoll, SatinRibbon, Felt
from homework_8.BouquetOfFlowers import BouquetOfFlowers
from homework_8.Flower import Rose
from homework_8.Flower import Tulip
from homework_8.Flower import Lily
from homework_8.Flower import Orchid

if __name__ == "__main__":
    bouquetOfFlowers = BouquetOfFlowers()
    rose = Rose(1000, 120)
    lily = Lily(1500, 150)
    orchid = Orchid(1300, 170)
    tulip = Tulip(1250, 120)
    kraftPaperRoll = KraftPaperRoll(200)
    satinRibbon = SatinRibbon(500)
    felt = Felt(500)
    bouquetOfFlowers.add_flower(rose)
    bouquetOfFlowers.add_flower(tulip)
    bouquetOfFlowers.add_flower(lily)
    bouquetOfFlowers.add_flower(orchid)
    bouquetOfFlowers.add_accessory(kraftPaperRoll)
    bouquetOfFlowers.add_accessory(satinRibbon)
    bouquetOfFlowers.add_accessory(felt)
    print('Среднее время увяданая:', bouquetOfFlowers.get_average_life_time())
    print('Сумма букета:', bouquetOfFlowers.get_total_price_of_flowers())
    sorted_flower_names = list(map(lambda f: f.name,
                                   bouquetOfFlowers.sort_flowers_by_price()))
    print('Отсортированный список цветов в букете по цене:',
          sorted_flower_names)
    print(bouquetOfFlowers.contains_specific_flower('Роза'))
