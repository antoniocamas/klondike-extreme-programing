from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number

class CardBuilder(object):

    def __init__(self):
        self._suit = Suit.CLOVERS
        self._number = Number.ACE
        self._faceUp = False


    def suit(self, suit):
        self._suit = suit
        return self

    def number(self, number):
        self._number = number
        return self

    def faceUp(self):
        self._faceUp = True
        return self


    def build(self):
        card = Card(self._suit, self._number)
        if self._faceUp:
            card.flip()
        return card
    
