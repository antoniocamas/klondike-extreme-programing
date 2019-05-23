import copy

class CardStackHelper(object):

    def __init__(self, cards):
        self._cards = cards

    @classmethod
    def fromCardStack(cls, cardstack):
        cardstack = copy.deepcopy(cardstack)
        cards = list()
        while not cardstack.empty():
            card = cardstack.pop()
            cards.append(card)

        cards.reverse()
        return cls(cards)

    def getCards(self):
        return self._cards

    def flip(self):
        for card in self._cards:
            card.flip()
        return self

    def reverse(self):
        self._cards.reverse()
        return self
    
