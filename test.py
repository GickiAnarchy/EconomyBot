from references import *

deck = Deck()

deck.createDeck()


while len(deck.cards) > 0:
    deck.drawCard()
    deck.shuffle()