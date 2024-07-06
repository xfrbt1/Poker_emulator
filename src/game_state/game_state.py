from src.game_state.combination_analyzer import Analyzer
from src.game_units.table import Table


class GameState:
    def __init__(self, n: int = 2):
        self.table: Table = Table(n)

        self.players_combination_mapping: dict[int, int] = {}
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

        count_max_values = sum(
            1
            for value in self.players_combination_mapping.values()
            if value == max(self.players_combination_mapping.values())
        )

        if count_max_values > 1:
            self.draws += 1

        #     """counting winners and make compare between same cards combinations players"""
        #     """for non sequence combinations make compare of values on hands players card O(n^2)"""
        #     """for all same combinations with a sequence, compare high card that sequence contains"""

        #     """make pool of players with same combinations"""
        #     """check if combination is a sequence or flush"""
        #     """make this sequence for all players and compare sequential last card"""
        #     """if this cards from players hand -> this player winner"""

        #     players_same_result = [
        #         k for k, v in self.players_combination_mapping.items() if v == max_value
        #     ]

        # elif count_max_values == 1:
        #     """1 person win, save data to database"""
