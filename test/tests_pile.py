import unittest
from tfd.card import Card
from tfd.suit import Suit
from tfd.number import Number
from tfd.test.card_builder import CardBuilder
from tfd.test.pile_builder import PileBuilder
from tfd.pile import Pile
        
class PileTest(unittest.TestCase):

    def test_GivenAndEmptyPile_WhenIsEmptyCalled_ReturnTrue(self):
        self.assertTrue(PileBuilder().build().empty())
        
    def test_GivenAndNotEmptyPile_WhenIsEmptyCalled_ReturnFalse(self):
        card = CardBuilder().build()
        self.assertFalse(PileBuilder().card(card).build().empty())

    def test_GivenAPileWithCardsFaceUp_WhenNumberOfFaceUpCards_ReturnTheRightNumber(self):
        card = CardBuilder().faceUp().build()
        self.assertEqual(PileBuilder().card(card).build().numberOfFaceUpCards(), 1)

    def test_GivenAPileWithoutCardsFaceUp_WhenNumberOfFaceUpCards_ReturnZero(self):
        card = CardBuilder().suit(Suit.HEARTS).build()
        self.assertEqual(PileBuilder().card(card).build().numberOfFaceUpCards(), 0)

    def test_GivenAPileWithoutCards_WhenNumberOfFaceUpCards_ReturnZero(self):
        card = CardBuilder().faceUp().build()
        self.assertEqual(PileBuilder().build().numberOfFaceUpCards(), 0)

    def test_GivenAPileWithoutCArds_WhengetTop_ThenEmptyListIsreturned(self):
        self.assertEqual(PileBuilder().build().getTop(1), [])
        
    def test_GivenAPileWithCards_WhengetTopWitlessCards_ThenTheRequestedNumberisReturned(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        returnedCards = PileBuilder().card(card).card(otherCard).card(topCard).build().getTop(2)
        self.assertListEqual(returnedCards, [otherCard, topCard])

    def test_GivenAPileWithCards_WhengetTopWithMoreCards_ThenAllArereturned(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        returnedCards = PileBuilder().card(card).card(otherCard).card(topCard).build().getTop(4)
        self.assertEqual(returnedCards, [card, otherCard, topCard])
        
    def test_GivenAEmtpyPile_WhenaddToTop_CardsAreAdded(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        cards = [card, otherCard, topCard]
        pile = PileBuilder().build()
        pile.addToTop(cards)
        
        self.assertEqual(pile.getTop(3), [card, otherCard, topCard])
        
    def test_GivenNotEmtpyPile_WhenaddToTop_CardsAreAdded(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        cards = [otherCard, topCard]
        pile = PileBuilder().card(card).build()
        pile.addToTop(cards)
        self.assertEqual(pile.getTop(3), [card, otherCard, topCard])

    def test_GivenNotEmtpyPile_WhenremoveTop_CardsAreRemoved(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        cards = [card, otherCard, topCard]
        pile = PileBuilder().card(card).card(otherCard).card(topCard).build()
        pile.removeTop(2)
        self.assertEqual(pile.getTop(3), [card])

    def test_GivenNotEmtpyPile_WhenremoveTop_TopCardisFaceUp(self):
        card = CardBuilder().build()
        otherCard = CardBuilder().suit(Suit.HEARTS).build()
        topCard = CardBuilder().suit(Suit.DIAMONDS).build()
        cards = [card, otherCard, topCard]
        pile = PileBuilder().card(card).card(otherCard).card(topCard).build()
        pile.removeTop(2)
        returnedCard = pile.getTop(3)[0]
        self.assertTrue(returnedCard.isFaceUp())

        
    def test_GivenEmtpyPile_WhenremoveTop_thePileStillEmpyt(self):
        pile = PileBuilder().build()
        pile.removeTop(1)
        self.assertTrue(pile.empty())


    def test_GivenAPileWithFaceUpDiamodQ_WhenCloverKAskIfFits_ReturnTrue(self):
        cardDQ = CardBuilder().suit(Suit.DIAMONDS).number(Number.QUEEN).faceUp().build()
        cardCK = CardBuilder().suit(Suit.CLOVERS).number(Number.KING).faceUp().build()
        pile = PileBuilder().card(cardDQ).build()
        self.assertTrue(pile.fitsIn(cardCK))
        
    def test_GivenAPileWithFaceDownDiamodQ_WhenCloverKAskIfFits_ReturnFalse(self):
        cardDQ = CardBuilder().suit(Suit.DIAMONDS).number(Number.QUEEN).build()
        cardCK = CardBuilder().suit(Suit.CLOVERS).number(Number.KING).faceUp().build()
        pile = PileBuilder().card(cardDQ).build()
        self.assertFalse(pile.fitsIn(cardCK))

    def test_GivenAPileWithFaceUpDiamodQ_WhenDIAMONDKAskIfFits_ReturnFalse(self):
        cardDQ = CardBuilder().suit(Suit.DIAMONDS).number(Number.QUEEN).faceUp().build()
        cardCK = CardBuilder().suit(Suit.DIAMONDS).number(Number.KING).faceUp().build()
        pile = PileBuilder().card(cardDQ).build()
        self.assertFalse(pile.fitsIn(cardCK))

    def test_GivenAEmptyPile_WhenKingAskIfFits_ReturnTrue(self):
        cardCK = CardBuilder().number(Number.KING).faceUp().build()
        pile = PileBuilder().build()
        self.assertTrue(pile.fitsIn(cardCK))

    def test_GivenAEmptyPile_WhenNotKingAskIfFits_ReturnFalse(self):
        cardCK = CardBuilder().number(Number.QUEEN).faceUp().build()
        pile = PileBuilder().build()
        self.assertFalse(pile.fitsIn(cardCK))
