import copy
from tfd import exception
from tfd.cardstack import CardStack
from tfd.suit import Suit
from tfd.number import Number

class Stock(object):

    def __init__(self, cards=list()):
        self._cardstack = CardStack(cards)

    def push(self, card):
        if card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        self._cardstack.push(card)
        
    def pop(self):
        return self._cardstack.pop()

    def peek(self):
        return self._cardstack.peek()

    def empty(self):
        return self._cardstack.empty()
        
    def getTop(self, numberOfCards):
        originalCards = copy.deepcopy(self._cardstack)
        retCards = list()
        for _ in range(numberOfCards):
            if not self.empty():
                retCards.append(originalCards.pop())
        return retCards

    def removeTop(self, numberOfCards):
        for _ in range(numberOfCards):
            if not self.empty():
                self.pop()
