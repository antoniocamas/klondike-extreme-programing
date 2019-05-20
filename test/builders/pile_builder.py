from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.pile import Pile
from builders.card_builder import CardBuilder
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
    
    def fill1Down4FaceUp(self):
        self.card(CardBuilder().number(Number.ACE).build())
        for suit, number in zip(Suit, reversed(Number)):
            self.card(CardBuilder().suit(suit).number(number).faceUp().build())
        return self

    def build(self):
        return Pile(self._number, self._cards)
    
