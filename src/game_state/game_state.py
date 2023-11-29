from typing import Dict

from src.game_state.combination_analyzer import Analyzer
from src.game_units.table import Table


class GameState:
    def __init__(self, n: int = 2):
        self.table: Table = Table(n)

        self.players_combination_mapping: Dict[int, int] = {}

    def update(self):
        self.table.renew_state()
        self.table.update_table()

    def analyze(self):
        print(self.table.table_cards)
        for i, player in enumerate(self.table.players.players_list):
            print(player)
            Analyzer.get_combination(player.cards, self.table.table_cards)
