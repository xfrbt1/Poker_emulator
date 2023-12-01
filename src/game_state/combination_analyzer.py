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
    def get_combination(player_cards: list[tuple], table_cards: list[tuple]):
        valued_list = create_valued_list(player_cards + table_cards)
        sorted_valued_list = sort_all_cards_asc(valued_list)

        if is_royal_flush(sorted_valued_list):
            return 10

        if is_straight_flush(sorted_valued_list):
            return 9

        if is_four_of_a_kind(sorted_valued_list):
            return 8

        if is_full_house(sorted_valued_list):
            return 7

        if is_flush(sorted_valued_list):
            return 6

        if is_straight(sorted_valued_list) or is_wheel(sorted_valued_list):
            return 5

        if is_three_of_a_kind(sorted_valued_list):
            return 4

        if is_two_pairs(sorted_valued_list):
            return 3

        if is_pair(sorted_valued_list):
            return 2

        return 1

    @staticmethod
    def get_winner(players_cards: list[list[tuple]]):
        ...
