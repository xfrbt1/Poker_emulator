class Player:
    def __init__(self):
        self.cards: list[tuple] = []

    def add_card(self, card: tuple):
        self.cards.append(card)

    def renew_cards(self):
        self.cards = []

    def __str__(self) -> str:
        string_repr = ""
        for card in self.cards:
            string_repr += f"{card}|"
        return string_repr

    def __len__(self):
        return len(self.cards)


class PlayersPool:
    def __init__(self, n: int = 2):
        self.n: int = n
        self.players_list: list[Player] | list = []

        self.create_players()

    def create_players(self):
        [self.players_list.append(Player()) for _ in range(self.n)]

    def renew_players(self):
        self.players_list = []
        self.create_players()
        [player.renew_cards() for player in self.players_list]

    def add_players_cards(self, cards_list: [list[tuple]]):
        if len(cards_list) % len(self) != 0:
            raise Exception("ERROR AMOUNT")
        for i in range(len(cards_list)):
            self.players_list[i % self.n].add_card(cards_list[i])

    def __len__(self) -> int:
        return self.n

    def print(self):
        [print(f"PLAYER {i}: ", player) for i, player in enumerate(self.players_list)]
