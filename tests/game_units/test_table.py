from src.game_units.deck import Deck


def test_add_cards_to_table(table):
    n_cards = 5
    table.add_cards_to_table(n_cards)
    assert len(table.table_cards) == n_cards
    assert table.deck.deck_amount == len(Deck.suits) * len(Deck.values) - n_cards
    assert table.deck.thrown_amount == n_cards


def test_add_cards_to_players(table):
    n_cards = 2
    table.add_cards_to_players(n_cards)
    assert (
        table.deck.deck_amount
        == len(Deck.suits) * len(Deck.values) - len(table.players) * n_cards
    )
    assert table.deck.thrown_amount == len(table.players) * n_cards


def test_renew_table(table):
    n_cards = 5
    table.add_cards_to_table(n_cards)
    assert len(table.table_cards) == n_cards

    table.renew_table()
    assert len(table.table_cards) == 0


def test_renew_state(table):
    n_cards_table = 5
    table.add_cards_to_table(n_cards_table)
    n_cards_players = 2
    table.add_cards_to_players(n_cards_players)
    assert table.deck.thrown_amount == n_cards_players * table.players.n + n_cards_table
