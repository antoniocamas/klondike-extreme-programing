from enum import Enum, unique
from tfd.color import Color

class Suit(Enum):
    HEARTS = (Color.RED, 'H')
    CLOVERS = (Color.BLACK, 'C')
    DIAMONDS = (Color.RED, 'D')
    PIKES = (Color.BLACK, 'P')


    def __init__(self, color, initial):
        self._color = color
        self._initial = initial

    def getColor(self):
        return self._color
