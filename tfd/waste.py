from tfd import exception
from tfd.cardstack import CardStack

class Waste(object):

    def __init__(self, cards):
        self._cardstack = CardStack(cards)

    def push(self, card):
        if not card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        self._cardstack.push(card)
        
    def pop(self):
        return self._cardstack.pop()

    def peek(self):
        return self._cardstack.peek()

    def empty(self):
        return self._cardstack.empty()
    
