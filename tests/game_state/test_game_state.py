import pytest


@pytest.mark.parametrize("game_state", [1, 2, 3, 4, 5], indirect=True)
def test_update(game_state):
    game_state.update()
    assert (
        game_state.table.deck.thrown_amount
        == game_state.table.table_cards_amount
        + game_state.table.players_amount * game_state.table.players_cards_amount
    )


# @pytest.mark.parametrize("game_state", [1, 2, 3, 4, 5], indirect=True)
# def test_analyze(game_state):
#     game_state.update()
#     game_state.analyze()
    # assert len(game_state.players_combination_mapping) == game_state.table.players_amount
