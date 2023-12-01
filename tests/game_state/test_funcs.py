import pytest

from src.game_state.combination_analyzer import Analyzer
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
from src.game_state.list_transformations import (
    create_valued_list,
    dict_counter,
    sort_all_cards_asc,
)


@pytest.mark.parametrize(
    "card_collection, predict_counter_suits, predict_counter_values",
    [
        (
            [("6", "S"), ("6", "C"), ("A", "S"), ("A", "C"), ("K", "S")],
            {"C": 2, "S": 3},
            {"6": 2, "A": 2, "K": 1},
        ),
        (
            [("5", "S"), ("5", "C"), ("5", "H"), ("A", "C"), ("A", "S")],
            {"C": 2, "S": 2, "H": 1},
            {"5": 3, "A": 2},
        ),
    ],
)
def test_dict_counter(card_collection, predict_counter_suits, predict_counter_values):
    counter_suits = dict_counter(card_collection, 1)
    counter_values = dict_counter(card_collection, 0)
    assert counter_suits == predict_counter_suits
    assert counter_values == predict_counter_values


@pytest.mark.parametrize(
    "card_collection, predict_result",
    [
        ([("J", "S")], [(11, "S")]),
        ([("Q", "S")], [(12, "S")]),
        ([("Q", "S"), ("K", "S"), ("A", "S")], [(12, "S"), (13, "S"), (14, "S")]),
    ],
)
def test_create_valued_list(card_collection, predict_result):
    assert create_valued_list(card_collection) == predict_result


@pytest.mark.parametrize(
    "card_collection, predict_result",
    [
        ([(13, "S"), (12, "S"), (10, "S")], [(10, "S"), (12, "S"), (13, "S")]),
        (
            [(10, "S"), (2, "C"), (5, "S"), (13, "D"), (2, "S")],
            [(2, "C"), (2, "S"), (5, "S"), (10, "S"), (13, "D")],
        ),
    ],
)
def test_sort_all_cards_asc(card_collection, predict_result):
    assert sort_all_cards_asc(card_collection) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("6", "C"), ("7", "C")],
            [("8", "C"), ("9", "C"), ("10", "C"), ("8", "D"), ("8", "H")],
            False,
        ),
        (
            [("J", "C"), ("Q", "C")],
            [("A", "C"), ("K", "C"), ("10", "C"), ("8", "D"), ("8", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("3", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "C"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("6", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("2", "S"), ("10", "D")],
            [("J", "D"), ("Q", "D"), ("K", "D"), ("A", "D"), ("A", "H")],
            False,
        ),
        (
            [("10", "S"), ("10", "H")],
            [("J", "D"), ("Q", "D"), ("K", "D"), ("A", "D"), ("A", "H")],
            False,
        ),
    ],
)
def test_is_royal_flush(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_royal_flush(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("6", "C"), ("7", "C")],
            [("8", "C"), ("9", "C"), ("10", "C"), ("8", "D"), ("8", "H")],
            True,
        ),
        (
            [("J", "C"), ("Q", "C")],
            [("A", "C"), ("K", "C"), ("10", "C"), ("8", "D"), ("8", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("3", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "C"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("6", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("2", "S"), ("10", "D")],
            [("J", "D"), ("Q", "D"), ("K", "D"), ("A", "D"), ("A", "H")],
            True,
        ),
        (
            [("10", "S"), ("10", "H")],
            [("J", "D"), ("Q", "D"), ("K", "D"), ("A", "D"), ("A", "H")],
            False,
        ),
    ],
)
def test_is_straight_flush(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_straight_flush(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("2", "S"), ("2", "C")],
            [("2", "D"), ("2", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("A", "C")],
            [("A", "D"), ("2", "H"), ("2", "S"), ("2", "D"), ("10", "H")],
            False,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_four_of_a_kind(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_four_of_a_kind(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("A", "S"), ("A", "S")],
            [("A", "D"), ("4", "S"), ("5", "S"), ("4", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("A", "D"), ("2", "H"), ("2", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
        (
            [("2", "S"), ("2", "C")],
            [("2", "D"), ("2", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_full_house(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_full_house(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_flush(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_flush(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("6", "S"), ("7", "S")],
            [("8", "S"), ("9", "S"), ("10", "S"), ("8", "D"), ("8", "H")],
            True,
        ),
        (
            [("10", "S"), ("J", "S")],
            [("Q", "S"), ("K", "S"), ("A", "S"), ("5", "D"), ("6", "S")],
            True,
        ),
        (
            [("6", "S"), ("7", "S")],
            [("8", "S"), ("9", "S"), ("10", "S"), ("5", "D"), ("2", "H")],
            True,
        ),
        (
            [("5", "C"), ("8", "S")],
            [("A", "D"), ("J", "H"), ("6", "C"), ("8", "D"), ("9", "S")],
            False,
        ),
        (
            [("3", "C"), ("3", "S")],
            [("3", "D"), ("4", "H"), ("5", "C"), ("6", "D"), ("9", "S")],
            False,
        ),
    ],
)
def test_is_straight(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_straight(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("A", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "S")],
            [("2", "S"), ("4", "S"), ("5", "S"), ("3", "D"), ("10", "H")],
            True,
        ),
        (
            [("2", "S"), ("2", "S")],
            [("3", "S"), ("4", "S"), ("5", "S"), ("A", "D"), ("10", "H")],
            True,
        ),
        (
            [("5", "C"), ("8", "S")],
            [("A", "D"), ("J", "H"), ("6", "C"), ("8", "D"), ("9", "S")],
            False,
        ),
        (
            [("3", "C"), ("3", "S")],
            [("3", "D"), ("4", "H"), ("5", "C"), ("6", "D"), ("9", "S")],
            False,
        ),
    ],
)
def test_is_wheel(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_wheel(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("2", "S"), ("2", "C")],
            [("2", "D"), ("3", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("A", "C")],
            [("A", "D"), ("2", "H"), ("2", "S"), ("2", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("A", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_three_of_a_kind(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_three_of_a_kind(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("2", "S"), ("2", "C")],
            [("3", "D"), ("3", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("A", "C")],
            [("A", "D"), ("2", "H"), ("2", "S"), ("3", "D"), ("3", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_two_pairs(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_two_pairs(sorted_valued_list) == predict_result


@pytest.mark.parametrize(
    "player_cards, table_cards, predict_result",
    [
        (
            [("2", "S"), ("2", "C")],
            [("3", "D"), ("3", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            True,
        ),
        (
            [("A", "S"), ("A", "C")],
            [("2", "D"), ("3", "H"), ("8", "S"), ("3", "D"), ("9", "H")],
            True,
        ),
        (
            [("A", "S"), ("2", "C")],
            [("3", "D"), ("4", "H"), ("5", "S"), ("9", "D"), ("10", "H")],
            False,
        ),
    ],
)
def test_is_pair(player_cards, table_cards, predict_result):
    valued_list = create_valued_list(player_cards + table_cards)
    sorted_valued_list = sort_all_cards_asc(valued_list)

    assert is_pair(sorted_valued_list) == predict_result
