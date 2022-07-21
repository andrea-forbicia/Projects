class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class Card:
    def __init__(self, code, credit):
        self.code = code
        self.credit = credit


class Column:
    def __init__(self, number, name, quantity):
        self.number = number
        self.name = name
        self.quantity = quantity


class Dispenser:
    def __init__(self):
        self.drinks = dict()
        self.cards = dict()
        self.columns = dict()

    def add_drink(self, code: str, name: str, price: float) -> None:
        drink = Drink(code=code, name=name, price=price)
        self.drinks[drink.code] = [drink.name, drink.price]

    def add_card(self, code: str, credit: float) -> None:
        card = Card(code=code, credit=credit)
        self.cards[card.code] = card.credit

    def add_column(self, number: int, drink_name: str, drink_quantity: int):
        column = Column(number=number, name=drink_name, quantity=drink_quantity)
        self.columns[column.number] = [column.name, column.quantity]

    def get_drink_price(self, drink_code: str) -> float:
        return self.drinks[drink_code][1]

    def get_drink_name(self, drink_code: str) -> str:
        return self.drinks[drink_code][0]

    def get_card_credit(self, card_code: str) -> float:
        return self.cards[card_code]

    def deliver_drink(self, drink_code: str, card_code: str) -> None:
        drink_name = self.get_drink_name(drink_code=drink_code)
        drink_price = self.get_drink_price(drink_code=drink_code)
        card_credit = self.get_card_credit(card_code=card_code)
        for column in self.columns.items():
            if column[0] == drink_name:
                card_credit -= drink_price
                column[1] -= 1
