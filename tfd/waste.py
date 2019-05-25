from tfd import exception

class Waste(object):

    def __init__(self, cards):
        self._cards = cards

    def push(self, card):
        if not card.isFaceUp():
            raise exception.InvalidCard(str(card))
        
        self._cards.append(card)
        
    def pop(self):
        return self._cards.pop()

    def peek(self):
        return self._cards[-1]

    def empty(self):
        return not self._cards
    
