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
        
    def empty(self):
        return not self._cards

    def getTop(self, numberOfCards=None):
        if not numberOfCards:
            return self._getLastCards(1)[0]
        
        return self._getLastCards(numberOfCards)
    
    def _getLastCards(self, numberOfCards):
        return [x for x in reversed(self._cards[-numberOfCards:])]

    def removeTop(self, numberOfCards=1):
        for _ in range(numberOfCards):
            if not self.empty():
                self._cards.pop()
