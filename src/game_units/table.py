from src.game_units.deck import Deck
from src.game_units.player import PlayersPool


class Table:
    def __init__(self, n: int = 2):
        self.deck: Deck = Deck()
        self.players: PlayersPool = PlayersPool(n)
        self.table_cards: list[tuple] = []

    def add_cards_to_table(self, n: int = 5):
        [self.table_cards.append(self.deck.pop()) for _ in range(n)]

    def add_cards_to_players(self, n: int = 2):
        self.players.add_players_cards(self.deck.pop_n(n * len(self.players)))

    def renew_table(self):
        self.table_cards = []

    def renew_state(self):
        self.deck.renew_deck()
        self.players.renew_players()
        self.renew_table()

    def update_table(self, n_cards_to_players: int = 2, n_cards_to_table: int = 5):
        self.add_cards_to_players(n_cards_to_players)
        self.add_cards_to_table(n_cards_to_table)

    def __str__(self) -> str:
        string_repr = "TABLE: "
        for card in self.table_cards:
            string_repr += f" {card}|"
        return string_repr

    def print_sate(self):
        self.players.print()
        print(self)

    @property
    def table_cards_amount(self) -> int:
        return len(self.table_cards)

    @property
    def players_amount(self) -> int:
        return len(self.players)

    @property
    def players_cards_amount(self) -> int:
        return len(self.players.players_list[0])
