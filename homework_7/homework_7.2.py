class ATM:
    NOMINALS = (100, 50, 20)

    def __init__(self, count_20=0, count_50=0, count_100=0):
        self.__bills = {20: count_20, 50: count_50, 100: count_100}

    def add_money(self, count_20=0, count_50=0, count_100=0):
        if min(count_20, count_50, count_100) < 0:
            raise ValueError("Количество купюр не может быть отрицательным")
        self.__bills[20] += count_20
        self.__bills[50] += count_50
        self.__bills[100] += count_100

    def __find_combination(self, amount):
        for n100 in range(min(self.__bills[100], amount // 100), -1, -1):
            after_100 = amount - n100 * 100
            for n50 in range(min(self.__bills[50], after_100 // 50), -1, -1):
                rest = after_100 - n50 * 50
                if rest % 20 == 0 and rest // 20 <= self.__bills[20]:
                    return {100: n100, 50: n50, 20: rest // 20}
        return None

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Сумма {amount}: некорректная сумма")
            return False

        combination = self.__find_combination(amount)
        if combination is None:
            print(f"Сумма {amount}: выдать невозможно")
            return False

        for nominal, count in combination.items():
            self.__bills[nominal] -= count

        issued = ", ".join(
            f"{nominal} x {count}"
            for nominal, count in combination.items() if count > 0
        )
        print(f"Сумма {amount}: выдано {issued}")
        return True

    def __str__(self):
        total = sum(n * c for n, c in self.__bills.items())
        return (f"В банкомате: "
                f"20 x {self.__bills[20]}, 50 x {self.__bills[50]}, "
                f"100 x {self.__bills[100]} (всего {total})")


if __name__ == "__main__":
    atm = ATM(count_20=5, count_50=2, count_100=3)
    print(atm)
    atm.add_money(count_20=2, count_50=1, count_100=1)
    print(atm)
    atm.withdraw(90)
    print(atm)
    atm.withdraw(60)
    print(atm)
    atm.withdraw(270)
    print(atm)
    atm.withdraw(35)
    print(atm)
    atm.withdraw(5000)
    print(atm)
