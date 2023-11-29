import pytest

from src.game_units.deck import Deck
from src.game_units.player import Player, PlayersPool
from src.game_units.table import Table


@pytest.fixture
def deck() -> Deck:
    deck = Deck()
    return deck


@pytest.fixture
def player() -> Player:
    player = Player()
    return player


@pytest.fixture
def players_pool() -> PlayersPool:
    players_pool = PlayersPool(2)
    return players_pool


@pytest.fixture
def table() -> Table:
    table = Table(2)
    return table
