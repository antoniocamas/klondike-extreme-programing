from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.stock import Stock

class StockBuilder(object):
    
    def __init__(self):
        self._cards = list()
    
    def getCards(self):
        return self._cards
                    
    def cards(self, numberOfCards):
        for suit, number in zip(Suit, Number):
            self._cards.append(Card(suit, number))
            if len(self._cards) == numberOfCards:
                return self
        return self

    def build(self):
        stock = Stock()
        for card in self._cards:
            stock.push(card)

        return stock
