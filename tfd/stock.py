import copy
from tfd import exception
from tfd.cardstack import CardStack
from tfd.suit import Suit
from tfd.number import Number

class Stock(CardStack):

    def __init__(self, cards=list()):
        super(Stock, self).__init__(cards)

    def push(self, card):
        if card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        super(Stock, self).push(card)
        
    def getTop(self, numberOfCards):
        originalCards = copy.deepcopy(self._cards)
        retCards = list()
        for _ in range(numberOfCards):
            if not self.empty():
                retCards.append(originalCards.pop())
        return retCards

    def removeTop(self, numberOfCards):
        for _ in range(numberOfCards):
            if not self.empty():
                self.pop()
