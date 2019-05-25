from random import shuffle
from tfd.suit import Suit
from tfd.foundation import Foundation
from tfd.pile import Pile
from tfd.waste import Waste
from tfd.stock import Stock
from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.error import Error

class Game(object):

    NUMBER_OF_PILES = 7
    
    def __init__(self):

        cards = list()
        for suit in Suit:
            for number in Number:
                cards.append(Card(suit, number))
                
        shuffle(cards)
        
        self._foundations = dict()
        for suit in Suit:
            self._foundations[suit] = Foundation(suit)

        self._piles = list()
        for index in range(1,self.NUMBER_OF_PILES+1):
            cardsForPile = list()
            for _ in range(index):
                cardsForPile.append(cards.pop())
            self._piles.append(Pile(index, cardsForPile))

        self._waste = Waste(list())
        self._stock = Stock(cards)
        
    def getFoundations(self):
        return self._foundations

    def getPiles(self):
        return self._piles

    def getWaste(self):
        return self._waste

    def getStock(self):
        return self._stock
    
    def isFinished(self):
        for suit in Suit:
            if not self._foundations[suit].isComplete():
                return False
        return True

    def clear(self):
        self.__init__()

    def moveFromStockToWaste(self):
        if self._stock.empty:
            return Error.EMPTY_STOCK
        
        cards = self._stock.takeTop(1)
        for card in cards:
            card.flip()
            self._waste.push(card)

    def moveFromWasteToFoundation(self, suit):
        if self._waste.empty():
            return Error.EMPTY_WASTE

        if not self._foundations[suit].isFittingIn(self._waste.getTop()):
            return Error.NO_FIT_FOUNDATION

        self._foundations[suit].push(self._waste.pop())

    def moveFromWasteToStock(self):
        if self._waste.empty():
            return Error.EMPTY_WASTE
        
        if not self._stock.empty():
            return Error.NO_EMPTY_STOCK

        cards = list()
        while not self._waste.empty():
            card = self._waste.pop()
            card.flip()
            cards.append(card)
            
        self._stock = Stock(cards)

    def moveFromWasteToPile(self, numberOfPile):
        if self._waste.empty():
            return Error.EMPTY_WASTE

        if not self._piles[numberOfPile-1].isFittingIn(self._waste.getTop()):
            return Error.NO_FIT_PILE

        self._piles[numberOfPile-1].push(self._waste.pop())

    def moveFromFoundationToPile(self, suit, numberOfPile):
        if self._foundations[suit].empty():
            return Error.EMPTY_FOUNDATION

        if not self._piles[numberOfPile-1].isFittingIn(self._foundations[suit].peek()):
            return Error.NO_FIT_PILE

        self._piles[numberOfPile-1].push(self._foundations[suit].pop())
        
    def moveFromPileToFoundation(self, numberOfPile, suit):
        if self._piles[numberOfPile-1].empty():
            return Error.EMPTY_PILE

        if not self._foundations[suit].isFittingIn(self._piles[numberOfPile-1].getTop()):
            return Error.NO_FIT_FOUNDATION

        self._foundations[suit].push(self._piles[numberOfPile-1].pop())

    def moveFromPileToPile(self,
                           pileNumberOrigin,
                           pileNumberDest,
                           numberOfCardsToMove):
        if pileNumberDest == pileNumberOrigin:
            return Error.SAME_PILE

        if self._piles[pileNumberOrigin-1].empty():
            return Error.EMPTY_PILE

        if self._piles[pileNumberOrigin-1].numberOfFaceUpCards() < numberOfCardsToMove:
            return Error.NO_ENOUGH_CARDS_PILE

        cardsToMove = self._piles[pileNumberOrigin-1].getTop(numberOfCardsToMove)
        if not self._piles[pileNumberDest-1].isFittingIn(cardsToMove[0]):
            return Error.NO_FIT_PILE

        self._piles[pileNumberOrigin-1].removeTop(numberOfCardsToMove)
        self._piles[pileNumberDest-1].addToTop(cardsToMove)
        self._piles[pileNumberOrigin-1].flipFirstCard()
