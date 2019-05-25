from tfd import exception
from tfd.number import Number

class Pile(object):

    def __init__(self, number, cards):
        self._cards = cards
        self._number = number
        self.flipFirstCard()

    def push(self, card):
        self._cards.append(card)
        
    def pop(self):
        return self._cards.pop()

    def empty(self):
        return not self._cards
    
    def getNumber(self):
        return self._number

    def getCards(self):
        return self._cards

    def numberOfFaceUpCards(self):
        numberOfFaceUpCards = 0
        for card in self.getCards():
            if card.isFaceUp():
                numberOfFaceUpCards = numberOfFaceUpCards + 1
            
        return numberOfFaceUpCards
        
        retCards = list()
        for count, card in enumerate(reversed(self.getCards())):
            if count == numberOfCards:
                return retCards
            retCards.insert(0, card)

        return retCards
    
    def getTop(self, numberOfCards=None):
        if not numberOfCards:
            return self._getLastCard()

        return self._getLastCards(numberOfCards)
    
    def _getLastCard(self):
        return self._cards[-1]
    
    def _getLastCards(self, numberOfCards):
        retCards = list()
        for count, card in enumerate(reversed(self.getCards())):
            if count == numberOfCards:
                return retCards
            retCards.insert(0, card)

        return retCards

    def addToTop(self, cards):
        for card in cards:
            if not card.isFaceUp():
                raise exception.InvalidCard(str(card))
            self.push(card)
            
    def removeTop(self, numberOfCards):
        if not numberOfCards:
            return
        
        for count in range(numberOfCards):
            if not self.empty():
                self.pop()

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
