from tfd import exception
from tfd.cardstack import CardStack
from tfd.suit import Suit
from tfd.number import Number

class Foundation(CardStack):

    CARDS_PER_SUIT = 13

    def __init__(self, suit):
        super(Foundation, self).__init__(list())
        self._suit = suit

    def push(self, card):
        if not card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        super(Foundation, self).push(card)
        
    def getSuit(self):
        return self._suit

    def isComplete(self):
        return len(self._cards) == self.CARDS_PER_SUIT

    def isFittingIn(self, card):
        if not card.isFaceUp() or self._suit != card.getSuit():
            return False
        
        if self.empty():
           if card.isSameNumber(Number.ACE):
               return True
           else:
               return False

        if card.isNextTo(self.peek()):
            return True

        return False
