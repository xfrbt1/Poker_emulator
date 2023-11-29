from typing import Dict
from game_units.player import Player
from src.game_units.table import Table


class GameState:
    def __init__(self, n: int = 2):
        self.table: Table = Table(n)

        self.players_combination_mapping: Dict[int, int] = {}

    def update(self):
        self.table.renew_state()
        self.table.update_table()

    def analyze(self):
        for i, player in enumerate(self.table.players.players_list):
            self.get_combination(player.cards, self.table.table_cards)

    @staticmethod
    def get_combination(pl: list[tuple], table_cards: list[tuple]):

        all_cards = pl + table_cards
        counter_values = {}
        counter_suits = {}

        valued_list = _create_valued_list(all_cards)
        sorted_valued_list = _sort_all_cards_asc(valued_list)

        for card in sorted_valued_list:
            _add_to_dict_counter(card[0], counter_values)
            _add_to_dict_counter(card[1], counter_suits)


def _add_to_dict_counter(value: str, collection: dict):
    if value in collection.keys():
        collection[value] += 1
        return
    collection[value] = 1


def _create_valued_list(card_collection: list[tuple]) -> list[tuple]:
    valued_card_collection = [(values.get(card[0]), card[1])
                              if values.get(card[0]) is not None
                              else (int(card[0]), card[1])
                              for card in card_collection]
    return valued_card_collection


def _sort_all_cards_asc(valued_card_collection: list[tuple]):
    sorted_list = sorted(valued_card_collection, key=lambda x: x[0])
    return sorted_list


combinations = {
    1: "HIGH CARD",
    2: "ONE PAIR",
    3: "TWO PAIRS",
    4: "THREE OF A KIND",
    5: "STRAIGHT",
    6: "FLUSH",
    7: "FULL HOUSE",
    8: "FOUR OF A KIND",
    9: "STRAIGHT FLUSH",
    10: "FLUSH ROYAL"
}


values = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}