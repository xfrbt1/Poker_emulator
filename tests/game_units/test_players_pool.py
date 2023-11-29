import pytest


def test_renew_players(players_pool):
    players_pool.renew_players()
    assert len(players_pool) == 2


def test_add_players_cards_failure(players_pool):
    with pytest.raises(Exception):
        players_pool.add_players_cards(
            [("4", "C"), ("A", "H"), ("J", "H"), ("6", "S"), ("9", "D")]
        )


def test_add_players_cards(players_pool):
    players_pool.add_players_cards([("4", "C"), ("A", "H"), ("J", "H"), ("6", "S")])
    assert players_pool.players_list[0].cards == [("4", "C"), ("J", "H")]
    assert players_pool.players_list[1].cards == [("A", "H"), ("6", "S")]
