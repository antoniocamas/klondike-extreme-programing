from tfd.cardstack import CardStack
from tfd.suit import Suit
from tfd.number import Number

class Foundation(CardStack):

    def __init__(self, suit):
        super(Foundation, self).__init__(list())
        self._suit = suit

    def getSuit(self):
        return self._suit

    def isComplete(self):
        return len(self._cards) == 13

    def fitsIn(self, card):
        if self._suit != card.getSuit():
            return False

        if self.empty():
           if card.getNumber() == Number.ACE:
               return True
           else:
               return False

        if self.peek().getNumber().getValue() + 1 == card.getNumber().getValue():
            return True
