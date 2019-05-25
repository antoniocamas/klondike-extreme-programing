from tfd import exception
from tfd.cardstack import CardStack
from tfd.number import Number

class Pile(CardStack):

    def __init__(self, number, cards):
        super(Pile, self).__init__(cards)
        self._number = number
        self.flipFirstCard()

    def getNumber(self):
        return self._number

    def getCards(self):
        return self._cards

    def numberOfFaceUpCards(self):
        numberOfFaceUpCards = 0
        for card in self._cards:
            if card.isFaceUp():
                numberOfFaceUpCards = numberOfFaceUpCards + 1
            
        return numberOfFaceUpCards
                
    def getTop(self, numberOfCards):
        retCards = list()
        for count, card in enumerate(reversed(self._cards)):
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
            if self._cards:
                self.pop()

    def isFittingIn(self, card):
        if not card.isFaceUp():
            return False
        
        if self.empty():
            if card.getNumber() == Number.KING:
                return True
            else:
                return False
        
        if not self.peek().isFaceUp():
            return False
        
        if (not self.peek().isSameColor(card)) and \
           self.peek().isNextTo(card):
            return True
        
        return False

    def flipFirstCard(self):
        if not self._cards:
            return
        
        if not self._cards[-1].isFaceUp():
            self._cards[-1].flip()
