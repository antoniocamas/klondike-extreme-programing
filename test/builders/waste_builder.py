from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.waste import Waste

class WasteBuilder(object):
    
    def __init__(self):
        self._cards = list()

    def card(self, card):
        self._cards.append(card)

    def build(self):
        waste = Waste()
        for card in self._cards:
            waste.addToTop(card)
        return waste
