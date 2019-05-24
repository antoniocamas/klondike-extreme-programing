from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.foundation import Foundation
from builders.card_builder import CardBuilder

class FoundationBuilder(object):

    def __init__(self):
        self._suit = Suit.PIKES
        self._cards = list()

    def suit(self, suit):
        self._suit = suit
        return self
        
    def card(self, card):
        self._cards.append(card)
        return self
    
    def cards(self, numberOfCards):
        for number in Number:
            card = CardBuilder().suit(self._suit).number(number).faceUp().build()
            self.card(card)
            if len(self._cards) == numberOfCards:
                return self
        return self

    def build(self):
        foundation = Foundation(self._suit)
        for card in self._cards:
            foundation.push(card)

        return foundation
    
