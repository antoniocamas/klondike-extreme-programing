from tfd import exception

class Waste(object):

    def __init__(self):
        self._cards = list()

    def addToTop(self, card):
        if not card.isFaceUp():
            raise exception.InvalidCard(str(card))

        self._cards.append(card)

    def getTop(self):
        return self._cards[-1]

    def removeTop(self):
        self._cards.pop()

    def isEmpty(self):
        return not self._cards
