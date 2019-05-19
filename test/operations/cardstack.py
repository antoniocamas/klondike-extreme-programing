import copy

class CardStackOperations(object):

    def __init__(self, cardstack):
        self._cardstack = copy.deepcopy(cardstack)

    def getCards(self):
        cardstack = copy.deepcopy(self._cardstack)
        cards = list()
        while not cardstack.empty():
            card = cardstack.pop()
            cards.append(card)
        return cards

    def getFlippedCards(self):
        cards = self.getCards()
        for card in cards:
            card.flip()
        return cards
    
