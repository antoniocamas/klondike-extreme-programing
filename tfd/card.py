from tfd.suit import Suit
from tfd.number import Number

class Card(object):

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        self._faceUp = False


    def __eq__(self, other):
        if self._suit == other._suit and \
           self._number == other._number:
            return True

        return False

    def __repr__(self):
        return self.toString()

    def getNumber(self):
        return self._number

    def getSuit(self):
        return self._suit
    
    def getColor(self):
        return self._suit.getColor()
        
    def flip(self):
        self._faceUp = not self._faceUp

    def isFaceUp(self):
        return self._faceUp
        

    def isNextTo(self, otherCard):
        if self._suit != otherCard._suit:
            return False

        if otherCard._number.getValue() +1 == self._number.getValue():
            return True

        return False

    def toString(self):
        return "{} {}".format(str(self._suit), str(self._number))
