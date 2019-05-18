from tfd.card import Card

class CardStack(object):

    def __init__(self, cards):
        self._cards = cards

    def push(self, card):
        self._cards.append(card)

    def pop(self):
        return self._cards.pop()

    def peek(self):
        return self._cards[-1]

    def empty(self):
        return not self._cards


