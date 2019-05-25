import copy
from tfd import exception
from tfd.suit import Suit
from tfd.number import Number

class Stock(object):

    def __init__(self, cards=list()):
        self._cards = cards

    def push(self, card):
        if card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        self._cards.append(card)
        
    def pop(self):
        return self._cards.pop()

    def peek(self):
        return self._cards[-1]

    def empty(self):
        return not self._cards
        
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
