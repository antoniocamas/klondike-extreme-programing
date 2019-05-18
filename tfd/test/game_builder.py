from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.foundation import Foundation
from tfd.pile import Pile
from tfd.waste import Waste
from tfd.stock import Stock
from tfd.game import Game
from tfd.test.foundation_builder import FoundationBuilder
from tfd.test.pile_builder import PileBuilder
from tfd.test.card_builder import CardBuilder

class GameBuilder(object):

    def __init__(self):
        self._game = Game()
        self._foundations = {
            Suit.HEARTS: FoundationBuilder().suit(Suit.HEARTS).build(),
            Suit.DIAMONDS: FoundationBuilder().suit(Suit.DIAMONDS).build(),
            Suit.CLOVERS: FoundationBuilder().suit(Suit.CLOVERS).build(),
            Suit.PIKES: FoundationBuilder().suit(Suit.PIKES).build()
        }

        self._waste = None
        self._stock = None


    def foundationEmpty(self, suit=Suit.PIKES):
        self._foundations[suit] = FoundationBuilder().build()
        return self
    
    def foundationComplete(self, suit=Suit.PIKES):
        
        self._foundations[suit] = FoundationBuilder().suit(suit).cards(13).build()
        return self

    def finished(self):
        for suit in Suit:
            self.foundationComplete(suit)
        return self

    def stockEmpty(self):
        self._stock = Stock()
        return self

    def stockNotEmpty(self):
        self._stock = Stock([CardBuilder().build()])
        return self

    def wasteWithAce(self, suit):
        card = CardBuilder().suit(suit).number(Number.ACE).build()
        self.cardInWaste(card)
        return self

    def cardInWaste(self, card):
        if not card.isFaceUp():
            card.flip()
        if not self._waste:
            self._waste = Waste(list())

        self._waste.push(card)

        return self

    def wasteNotEmpty(self):
        cards = list()
        for suit, number in zip(Suit, Number):
            cards.append(CardBuilder().suit(suit).number(number).build())
            cards[-1].flip()
        self._waste = Waste(cards)
        return self

    def cardInPile(self, pileNumber, card):
        self._game._piles[pileNumber-1].push(card)
        return self

    def pileEmpty(self, pileNumber):
        self._game._piles[pileNumber-1] = PileBuilder().build()
        return self
        

    def build(self):
        self._game._foundations = self._foundations
        if self._stock:
            self._game._stock = self._stock
        if self._waste:
            self._game._waste = self._waste
        return self._game
