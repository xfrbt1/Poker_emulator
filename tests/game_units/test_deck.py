import pytest

from src.game_units.deck import Deck


def test_create_deck(deck):
    assert deck.deck_amount == len(Deck.suits) * len(Deck.values)


def test_pop(deck):
    card = deck.pop()
    assert card == deck.thrown[0]

    deck.renew_deck()
    assert deck.deck_amount == len(Deck.suits) * len(Deck.values)


def test_pop_n(deck):
    deck.pop_n(52)
    assert deck.deck_amount == 0

    deck.renew_deck()
    assert deck.deck_amount == len(Deck.suits) * len(Deck.values)


@pytest.mark.skip
def test_renew_deck_exception(deck):
    deck.deck.append((Deck.suits[1], Deck.suits[0]))

    with pytest.raises(Exception):
        deck.renew_deck()


def test_renew_deck(deck):
    deck.renew_deck()
    assert deck.thrown_amount == 0
    assert deck.deck_amount == len(Deck.suits) * len(Deck.values)

    assert deck.check_uniques() is True
    assert deck.check_len() is True
