class CreditCard:
    def __init__(self, card_number: str, balance: float):
        self.__card_number = card_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            self.__balance = 0
        else:
            self.__balance -= amount

    def show_info(self):
        print(f"Номер карты: {self.__card_number}, баланс: {self.__balance}")


credit_card = CreditCard('1', 22)
credit_card.withdraw(10)
credit_card.show_info()
credit_card.withdraw(2)
credit_card.show_info()
credit_card.withdraw(30)
credit_card.show_info()
credit_card.deposit(15)
credit_card.show_info()
