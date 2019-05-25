from tfd import exception
from tfd.suit import Suit
from tfd.number import Number

class Stock(object):

    def __init__(self, cards=list()):
        self._cards = cards

    def addToTop(self, card):
        if card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        self._cards.append(card)
        
    def pop(self):
        return self._cards.pop()

    def empty(self):
        return not self._cards
        
    def getTop(self, numberOfCards):
        return [x for x in reversed(self._cards[-numberOfCards:])]

    def removeTop(self, numberOfCards):
        for _ in range(numberOfCards):
            if not self.empty():
                self.pop()
