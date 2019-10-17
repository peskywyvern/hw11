import random


class Client:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show_total_balance(self):
        return sum([card.balance for card in self.cards])


class Card:
    def __init__(self, owner: Client, bank):
        self.account = random.randint(0, 99999)
        self.balance = 0.0
        self.pin = 0000
        self.owner = owner
        self.bank = bank

    def transfer_money(self, card, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            card.balance += amount
        else:
            print('operation impossible')


class Bank:
    def __init__(self, name):
        self.name = name
        self.client_accounts = set()

    def open_account(self, client: Client):
        if client not in self.client_accounts:
            new_card = Card(client, self)
            self.client_accounts.add(client)
            client.cards.append(new_card)
            return new_card

    def close_account(self, card: Card):
        self.client_accounts.remove(card.owner)


class ATM:
    def __init__(self, bank: Bank, amount: float):
        self.bank = bank
        self.amount = amount

    def withdraw(self, card: Card, sum: float):
        if sum <= card.balance:
            card.balance -= sum
            self.amount += sum
        else:
            print('operation impossible')

    def add(self, card: Card, sum: float):
        if sum <= self.amount:
            card.balance += sum
            self.amount -= sum
        else:
            print('operation impossible')

    def change_pin(self, card: Card, old_pin: int, new_pin: int):
        if card.pin == old_pin:
            card.pin = new_pin
        else:
            print('pin is not valid')


client = Client("John")
bank = Bank("PrivatBank")
atm = ATM(bank, 10000)

card = bank.open_account(client)
assert card.balance == 0.0

atm.add(card, 500)
assert card.balance == 500.0
