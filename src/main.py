from deck.card import Card
from deck.deck import Deck

deck = Deck()

deck.create_deck()
deck.shuffle_deck()

deck.print()
print(deck.deck_amount)
print(deck.thrown_amount)
print('_____________')

card = deck.pop()
print('card: ', card)
print('_____________')


print('_____________')

card = deck.pop()
print('card: ', card)
print('_____________')

print('_____________')

card = deck.pop()
print('card: ', card)
print('_____________')
print('_____________')

card = deck.pop()
print('card: ', card)
print('_____________')

deck.print()
print('_____________')
print(deck.thrown_amount)
print(deck.deck_amount)