from random import shuffle

from card import Card


class Deck:
    suits = ['S', 'H', 'D', 'C']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self._deck: list[Card] | list = []
        self._thrown: list[Card] | list = []

    def create_deck(self):
        self._deck: list[Card] = [Card(value, suit) for suit in Deck.suits for value in Deck.values]

    def shuffle_deck(self):
        shuffle(self._deck)

    def pop(self) -> Card | None:
        if len(self._deck) == 0:
            return None

        card = self._deck.pop(len(self._deck) - 1)

        self._thrown.append(card)
        return card

    def get_notation(self, index: int):
        return f"{self._deck[index].value}{self._deck[index].suit}"

    def print(self):
        [print(card) for card in self._deck]

    @property
    def deck_amount(self) -> int:
        return len(self._deck)

    @property
    def thrown_amount(self) -> int:
        return len(self._thrown)


