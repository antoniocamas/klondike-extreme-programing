from tfd import exception
from tfd.number import Number

class Pile(object):

    def __init__(self, number, cards):
        self._cards = cards
        self._number = number
        self.flipFirstCard()

    def empty(self):
        return not self._cards
    
    def getNumber(self):
        return self._number

    def numberOfFaceUpCards(self):
        numberOfFaceUpCards = 0
        for card in self._cards:
            if card.isFaceUp():
                numberOfFaceUpCards = numberOfFaceUpCards + 1
            
        return numberOfFaceUpCards
    
    def getTop(self, numberOfCards=None):
        if not numberOfCards:
            return self._getLastCards(1)[0]

        return self._getLastCards(numberOfCards)
    
    def _getLastCards(self, numberOfCards):
        return self._cards[-numberOfCards:]

    def addToTop(self, cards):
        if type(cards) != list:
            cards = [cards]
            
        for card in cards:
            if not card.isFaceUp():
                raise exception.InvalidCard(str(card))
            self._cards.append(card)
            
    def removeTop(self, numberOfCards=1):
        for count in range(numberOfCards):
            if not self.empty():
                self._cards.pop()

    def isFittingIn(self, card):
        if not card.isFaceUp():
            return False
        
        if self.empty():
            if card.isSameNumber(Number.KING):
                return True
            else:
                return False
        
        if not self.getTop().isFaceUp():
            return False
        
        if (not self.getTop().isSameColor(card)) and \
           self.getTop().isNextTo(card):
            return True
        
        return False

    def flipFirstCard(self):
        if self.empty():
            return
        
        if not self.getTop().isFaceUp():
            self.getTop().flip()
