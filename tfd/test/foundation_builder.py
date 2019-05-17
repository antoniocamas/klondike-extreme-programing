from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.foundation import Foundation

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
            self._cards.append(Card(self._suit, number))
            if len(self._cards) == numberOfCards:
                return self
        return self

    def build(self):
        foundation = Foundation(self._suit)
        for card in self._cards:
            foundation.push(card)

        return foundation
    
