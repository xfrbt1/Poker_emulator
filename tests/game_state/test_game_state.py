import pytest

from src.game_state.combination_analyzer import Analyzer


@pytest.mark.parametrize("game_state", [1, 2, 3, 4, 5], indirect=True)
def test_update(game_state):
    game_state.update()
    assert (
        game_state.table.deck.thrown_amount
        == game_state.table.table_cards_amount
        + game_state.table.players_amount * game_state.table.players_cards_amount
    )


@pytest.mark.parametrize(
    "player_cards, table_cards, predict",
    [
        (
            [("6", "H"), ("10", "S")],
            [("K", "H"), ("8", "H"), ("5", "H"), ("K", "S"), ("A", "S")],
            2,
        ),
        (
            [("2", "C"), ("9", "H")],
            [("K", "H"), ("8", "H"), ("5", "H"), ("K", "S"), ("A", "S")],
            2,
        ),
        (
            [("9", "S"), ("10", "C")],
            [("10", "S"), ("10", "D"), ("A", "S"), ("7", "S"), ("4", "C")],
            4,
        ),
        (
            [("A", "D"), ("K", "C")],
            [("10", "S"), ("10", "D"), ("A", "S"), ("7", "S"), ("4", "C")],
            3,
        ),
        (
            [("A", "S"), ("Q", "H")],
            [("J", "S"), ("5", "C"), ("6", "D"), ("Q", "C"), ("9", "H")],
            2,
        ),
        (
            [("8", "D"), ("7", "C")],
            [("J", "S"), ("5", "C"), ("6", "D"), ("Q", "C"), ("9", "H")],
            5,
        ),
        (
            [("8", "D"), ("7", "S")],
            [("8", "C"), ("5", "C"), ("2", "H"), ("Q", "H"), ("4", "H")],
            2,
        ),
        (
            [("8", "S"), ("6", "D")],
            [("8", "C"), ("5", "C"), ("2", "H"), ("Q", "H"), ("4", "H")],
            2,
        ),
        (
            [("3", "D"), ("K", "S")],
            [("9", "S"), ("J", "C"), ("7", "D"), ("5", "C"), ("4", "S")],
            1,
        ),
        (
            [("8", "D"), ("J", "D")],
            [("9", "S"), ("J", "C"), ("7", "D"), ("5", "C"), ("4", "S")],
            2,
        ),
        (
            [("9", "D"), ("2", "D")],
            [("6", "C"), ("5", "S"), ("A", "S"), ("3", "D"), ("4", "C")],
            5,
        ),
        (
            [("A", "D"), ("Q", "C")],
            [("6", "C"), ("5", "S"), ("A", "S"), ("3", "D"), ("4", "C")],
            2,
        ),
        (
            [("6", "H"), ("7", "D")],
            [("6", "C"), ("10", "C"), ("K", "S"), ("3", "H"), ("7", "S")],
            3,
        ),
        (
            [("8", "C"), ("10", "H")],
            [("6", "C"), ("10", "C"), ("K", "S"), ("3", "H"), ("7", "S")],
            2,
        ),
        (
            [("K", "C"), ("5", "C")],
            [("3", "S"), ("A", "S"), ("J", "C"), ("2", "D"), ("4", "D")],
            5,
        ),
        (
            [("10", "H"), ("6", "C")],
            [("3", "S"), ("A", "S"), ("J", "C"), ("2", "D"), ("4", "D")],
            1,
        ),
        (
            [("K", "H"), ("7", "D")],
            [("6", "C"), ("5", "H"), ("9", "D"), ("6", "D"), ("6", "H")],
            4,
        ),
        (
            [("6", "S"), ("K", "S")],
            [("6", "C"), ("5", "H"), ("9", "D"), ("6", "D"), ("6", "H")],
            8,
        ),
    ],
)
def test_analyzer_get_combination(player_cards, table_cards, predict):
    assert Analyzer.get_combination(player_cards, table_cards) == predict
