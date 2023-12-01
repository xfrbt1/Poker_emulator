import pytest

from src.game_state.game_state import GameState


@pytest.fixture
def game_state(request):
    n_players = request.param
    game_state = GameState(n_players)
    return game_state
