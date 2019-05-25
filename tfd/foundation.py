from tfd import exception
from tfd.suit import Suit
from tfd.number import Number

class Foundation(object):

    CARDS_PER_SUIT = 13

    def __init__(self, suit):
        self._cards = list()
        self._suit = suit

    def push(self, card):
        if not card.isFaceUp():
            raise exception.InvalidCard(str(card))
        self._cards.append(card)
        
    def pop(self):
        return self._cards.pop()

    def getTop(self):
        return self._cards[-1]

    def empty(self):
        return not self._cards
        
    def getSuit(self):
        return self._suit

    def isComplete(self):
        return len(self._cards) == self.CARDS_PER_SUIT

    def isFittingIn(self, card):
        if (not card.isFaceUp()) or (not card.isSameSuit(self._suit)):
            return False
        
        if self.empty():
           if card.isSameNumber(Number.ACE):
               return True
           else:
               return False

        if card.isNextTo(self.getTop()):
            return True

        return False
