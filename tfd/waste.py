from tfd.cardstack import CardStack

class Waste(CardStack):

    def __init__(self, cards):
        super(Waste, self).__init__(cards)

    def push(self, card):
        if card.isFaceUp():
            super(Waste, self).push(card)
        
