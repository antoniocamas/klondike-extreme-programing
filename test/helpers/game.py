class GameHelper(object):

    CARDS_IN_GAME=52
    INITIAL_CARDS_IN_STOCK=24
    
    def __init__(self, game):
        self._game = game

    def isWasteInInitialState(self):
        return self._game.getWaste().isEmpty()
        
    def areFoundationsInitialState(self):
        foundations = self._game.getFoundations()
        for _, foundation in foundations.items():
            if not foundation.isEmpty():
                return False
        return True

    def arePilesInitialState(self):
        piles = self._game.getPiles()
        for pile in piles:
            if pile.getNumber() != len(pile.getTop(self.CARDS_IN_GAME)):
                return False
            if not pile.getTop().isFaceUp():
                return False
        return True

    def isStockInitialState(self):
        stock = self._game.getStock()
        if len(stock.getTop(24)) != self.INITIAL_CARDS_IN_STOCK:
            return False
        return stock.isEmpty
