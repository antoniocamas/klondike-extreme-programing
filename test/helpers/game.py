class GameHelper(object):

    def __init__(self, game):
        self._game = game

    def isWasteInInitialState(self):
        return self._game.getWaste().empty()
        
    def areFoundationsInitialState(self):
        foundations = self._game.getFoundations()
        for _, foundation in foundations.items():
            if not foundation.empty():
                return False
        return True

    def arePilesInitialState(self):
        piles = self._game.getPiles()
        for pile in piles:
            if pile.getNumber() != len(pile.getCards()):
                return False
            if not pile.peek().isFaceUp():
                return False
        return True

    def isStockInitialState(self):
        stock = self._game.getStock()
        if len(stock.getTopCards(24)) != 24:
            return False
        return stock.empty
