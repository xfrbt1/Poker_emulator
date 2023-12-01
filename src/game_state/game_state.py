from typing import Dict

from src.game_state.combination_analyzer import Analyzer
from src.game_units.table import Table


class GameState:
    def __init__(self, n: int = 2):
        self.table: Table = Table(n)

        self.players_combination_mapping: Dict[int, int] = {}
        self.draws = 0

    def update(self):
        self.players_combination_mapping = {}
        self.table.renew_state()
        self.table.update_table()

    def analyze(self):
        for i, player in enumerate(self.table.players.players_list):
            self.players_combination_mapping[i] = Analyzer.get_combination(
                player.cards, self.table.table_cards
            )

        max_value = max(self.players_combination_mapping.values())
        count_max_values = sum(
            1
            for value in self.players_combination_mapping.values()
            if value == max_value
        )

        if count_max_values > 1:
            self.draws += 1
