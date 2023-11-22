from src.deck.deck import Deck
from src.player.player import PlayersPool


class Table:
    def __init__(self, n: int = 3):
        self.deck: Deck | None = None
        self.players: PlayersPool | None = None
        self.table_card: list[tuple] = []

        self.init_units(n)

    def init_units(self, n: int):
        self.players = PlayersPool(n)
        self.deck = Deck()

    def add_cards_to_table(self, n: int = 3):
        [self.table_card.append(self.deck.pop()) for _ in range(n)]

    def add_cards_to_players(self, n: int = 2):
        self.players.add_players_cards(self.deck.pop_n(n * len(self.players)))

    def renew_table(self):
        self.table_card = []

    def renew_state(self):
        self.deck.renew_deck()
        self.players.renew_players()
        self.renew_table()

    def update_table(self):
        self.add_cards_to_players()
        self.add_cards_to_table()

    def __str__(self) -> str:
        string_repr = 'TABLE: '
        for card in self.table_card:
            string_repr += f" {card}|"
        return string_repr

    def print_sate(self):
        self.players.print()
        print(self)
