from tfd.cardstack import CardStack
from tfd.number import Number

class Pile(CardStack):

    def __init__(self, number, cards):
        super(Pile, self).__init__(cards)
        self._number = number
        self._numberOfFaceUpCards = None
        
    def getNumber(self):
        return self._number

    def getCards(self):
        return self._cards

    def numberOfFaceUpCards(self):
        self._numberOfFaceUpCards = 0
        for card in self._cards:
            if card.isFaceUp():
                self._numberOfFaceUpCards = self._numberOfFaceUpCards + 1
            
        return self._numberOfFaceUpCards
                
    def getTop(self, numberOfCards):
        retCards = list()
        for count, card in enumerate(reversed(self._cards)):
            if count == numberOfCards:
                return retCards
            retCards.insert(0, card)

        return retCards

    def addToTop(self, cards):
        for card in cards:
            self.push(card)
            
    def removeTop(self, numberOfCards):
        if not numberOfCards:
            return
        
        for count in range(numberOfCards):
            if self._cards:
                self.pop()

        self._flipFirstCard()


    def fitsIn(self, card):
        if not self._cards:
            if card.getNumber() == Number.KING:
                return True
            else:
                return False
        
        topCard = self.peek()
        
        if not topCard.isFaceUp():
            return False

        if topCard.getColor() == card.getColor():
            return False
        
        if topCard.getNumber().getValue() + 1 == card.getNumber().getValue():
            return True
        
        return False

    def _flipFirstCard(self):
        if not self._cards:
            return
        
        if not self._cards[-1].isFaceUp():
            self._cards[-1].flip()
