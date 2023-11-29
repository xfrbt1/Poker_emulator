import pytest

from src.game_state.combination_analyzer import Analyzer


@pytest.mark.parametrize(
    "card_collection, predict_counter_suits, predict_counter_values", [

        ([('6', 'S'), ('6', 'C'), ('A', 'S'), ('A', 'C'), ('K', 'S')],
         {'C': 2, 'S': 3},
         {'6': 2, 'A': 2, 'K': 1}),

        ([('5', 'S'), ('5', 'C'), ('5', 'H'), ('A', 'C'), ('A', 'S')],
         {'C': 2, 'S': 2, 'H': 1},
         {'5': 3, 'A': 2})
    ]
)
def test_dict_counter(card_collection, predict_counter_suits, predict_counter_values):

    counter_suits = Analyzer.dict_counter(card_collection, 1)
    counter_values = Analyzer.dict_counter(card_collection, 0)
    assert counter_suits == predict_counter_suits
    assert counter_values == predict_counter_values


def test_create_valued_list():
    ...


def test_sort_all_cards_asc():
    ...
