from random import shuffle


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"({self.value}, {self.suit})"


class Deck:
    suits = ['S', 'H', 'D', 'C']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck: list = []
        self.thrown: list = []

        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        [self.deck.append((value, suit)) for suit in Deck.suits for value in Deck.values]

    def create_deck_str(self):
        [self.deck.append(f"{value}{suit}") for suit in Deck.suits for value in Deck.values]

    def renew_deck(self):
        if self.thrown_amount > 0:
            self.from_thrown_to_deck()

        if not self.check_uniques():
            raise Exception("ERROR UNIQ")

        if not self.check_len():
            raise Exception("ERROR LEN")

        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)

    def from_thrown_to_deck(self):
        for i in range(self.thrown_amount):
            card = self.thrown.pop()
            self.deck.append(card)

    def check_uniques(self) -> bool:
        for i in range(self.deck_amount - 1):
            for j in range(i+1, self.deck_amount):
                if self.deck[i] == self.deck[j]:
                    return False
        return True

    def check_len(self) -> bool:
        if len(self.deck) != len(Deck.suits) * len(Deck.values):
            return False
        return True

    def pop(self) -> tuple | None:
        if self.deck_amount > 0:
            card = self.deck.pop()
            self.thrown.append(card)
            return card
        return None

    def pop_n(self, n: int = 2) -> list[tuple]:
        return [self.pop() for _ in range(n)]

    @property
    def deck_amount(self) -> int:
        return len(self.deck)

    @property
    def thrown_amount(self) -> int:
        return len(self.thrown)

    def print(self):
        for card in self.deck:
            print(card, end=' ')
        print('\n')


