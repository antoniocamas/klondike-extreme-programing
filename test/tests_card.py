import unittest
from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from builders.card_builder import CardBuilder
        
class CardTest(unittest.TestCase):


    def test_Given2CardsThatAreEqual_WhenCompared_ReturnTrue(self):

        card = CardBuilder().build()
        otherCard = CardBuilder().build()

        self.assertTrue(card==otherCard)
    
    def test_Given2CardsDifferent_WhenCompared_ReturnFalse(self):

        card = CardBuilder().suit(Suit.HEARTS).build()
        otherCard = CardBuilder().suit(Suit.DIAMONDS).build()

        self.assertFalse(card==otherCard)
        
    def test_GivenACard_Whenfliped_isFaceUpChanges(self):
        card = CardBuilder().build()
        self.assertFalse(card.isFaceUp())
        card.flip()
        self.assertTrue(card.isFaceUp())

    def test_GivenACardandTheNExt_WhenisNextToCalled_ReturnTrue(self):
        card = CardBuilder().suit(Suit.PIKES).number(Number.QUEEN).build()
        cardOther = CardBuilder().suit(Suit.PIKES).number(Number.JACK).build()
        self.assertTrue(card.isNextTo(cardOther))

    def test_GivenACardandNotTheNExt_WhenisNextToCalled_ReturnFalse(self):
        card = CardBuilder().suit(Suit.PIKES).number(Number.QUEEN).build()
        cardOther = CardBuilder().suit(Suit.PIKES).number(Number.JACK).build()
        self.assertFalse(cardOther.isNextTo(card))

    def test_GivenACard_WhenConvertedToString_ThenTheStrIsReturned(self):
        card = CardBuilder().build()
        self.assertEqual(card.toString(), "Suit.CLOVERS Number.ACE D")

