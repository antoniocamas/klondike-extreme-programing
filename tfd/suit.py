from enum import Enum, unique
from tfd.color import Color

_INITIALS = []

class Suit(Enum):
    HEARTS = (Color.RED, 'H')
    DIAMONDS = (Color.RED, 'D')
    CLOVERS = (Color.BLACK, 'C')
    PIKES = (Color.BLACK, 'P')

    
    def __init__(self, color, initial):
        self._color = color
        self._initial = initial
        _INITIALS.append(initial)

    @classmethod
    def initials(cls):
        return _INITIALS

    def getColor(self):
        return self._color

    @staticmethod
    def find(initial):
        for suit in Suit:
            if initial == suit._initial:
                return suit
        return None
        

                                                        
