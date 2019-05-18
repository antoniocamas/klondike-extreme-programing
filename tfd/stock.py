from tfd.cardstack import CardStack
from tfd.suit import Suit
from tfd.number import Number

class Stock(CardStack):

    def __init__(self):
        super(Stock, self).__init__(list())

    def takeTop(self, numberOfCards):
        retCards = list()
        for _ in range(numberOfCards):
            if not self.empty():
                retCards.append(self.pop())
        return retCards
