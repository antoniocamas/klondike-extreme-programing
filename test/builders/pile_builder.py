from tfd.card import Card
from tfd.suit import Suit
from tfd.pile import Pile

class PileBuilder(object):

    def __init__(self):
        self._number = 1
        self._cards = list()

    def card(self, card):
        self._cards.append(card)
        return self

    def number(self, number):
        self._number = number
        return self

    def build(self):
        return Pile(self._number, self._cards)
    
