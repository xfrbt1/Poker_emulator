from typing import Callable

from src.game_state.combinations_func import (
    is_flush,
    is_four_of_a_kind,
    is_full_house,
    is_pair,
    is_royal_flush,
    is_straight,
    is_straight_flush,
    is_three_of_a_kind,
    is_two_pairs,
    is_wheel,
)
from src.game_state.list_transformations import create_valued_list, sort_all_cards_asc


class Analyzer:
    @staticmethod
    def get_combination(player_cards: list[tuple], table_cards: list[tuple]) -> int:
        valued_list: list[tuple] = create_valued_list(player_cards + table_cards)
        sorted_valued_list: list[tuple] = sort_all_cards_asc(valued_list)
        return Analyzer.get_combination_value(sorted_valued_list)

    @staticmethod
    def get_combination_value(sorted_valued_list: list[tuple]) -> int:
        mapping: dict[Callable, int] = {
            is_royal_flush: 10,
            is_straight_flush: 9,
            is_four_of_a_kind: 8,
            is_full_house: 7,
            is_flush: 6,
            is_straight: 5,
            is_wheel: 5,
            is_three_of_a_kind: 4,
            is_two_pairs: 3,
            is_pair: 2,
        }

        for key in mapping.keys():
            if key(sorted_valued_list):
                return mapping[key]
        else:
            return 1

    @staticmethod
    def get_winner(players_cards: list[list[tuple]]):
        ...
