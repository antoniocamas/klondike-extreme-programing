from tfd.suit import Suit
from tfd.number import Number

class Card(object):

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        self._faceUp = False

    def __eq__(self, other):
        if self._suit == other._suit and \
           self.isSameNumber(other._number) and \
           self._faceUp == other._faceUp:
            return True

        return False

    def __repr__(self):
        return self.toString()

    def getSuit(self):
        return self._suit
    
    def flip(self):
        self._faceUp = not self._faceUp

    def isFaceUp(self):
        return self._faceUp

    def isNextTo(self, otherCard):
        if otherCard._number.getValue() +1 == self._number.getValue():
            return True

        return False

    def isSameColor(self, otherCard):
        return self._suit.getColor() == otherCard._suit.getColor()

    def isSameNumber(self, number):
        return self._number == number

    def toString(self):
        return "{} {} {}".format(
            str(self._suit), str(self._number),
            "U" if self.isFaceUp() else "D")
