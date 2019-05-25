from enum import Enum, unique

@unique
class Error(Enum):

    EMPTY_STOCK = ("The stock is empty")
    EMPTY_WASTE = ("The waste is empty")
    EMPTY_FOUNDATION = ("The foundation is empty")
    EMPTY_PILE = ("The pile is empty")
    NO_EMPTY_STOCK = ("The stock is not empty")
    NO_FIT_FOUNDATION = ("It doesn't fit in the foundation")
    NO_FIT_PILE = ("It doesn't fit in the Pile")
    SAME_PILE = ("It is the same Pile")
    NO_ENOUGH_CARDS_PILE = ("Not enough cards in the pile")

    def __init__(self, message):
        self._message = message

    def getMessage(self):
        return self._message
