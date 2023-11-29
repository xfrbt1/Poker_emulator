def test_add_cards(player, deck):
    player.add_card(deck.pop())
    assert len(player) == 1

    player.renew_cards()
    assert len(player) == 0


def test_renew_cards(player, deck):
    player.add_card(deck.pop())
    assert len(player) == 1
    assert deck.thrown_amount == 1

    player.renew_cards()
    deck.renew_deck()
    assert len(player) == 0
    assert deck.thrown_amount == 0
