import unittest
from tfd.suit import Suit
from tfd.color import Color

class SuitTests(unittest.TestCase):

    def test_GivenASuitwithInitials_WhenInitials_ThenReturnedInitials(self):
        self.assertEqual(Suit.initials(), ['H', 'D', 'C', 'P'])

    def test_getColor(self):
        self.assertEqual(Suit.HEARTS.getColor(), Color.RED)

    def test_GivenAInitialH_ReturnTheSuitHeart(self):
        self.assertEqual(Suit.find('H'), Suit.HEARTS)

    def test_GivenAInitialNotExistant_returnNone(self):
        self.assertIsNone(Suit.find('A'))



import unittest
from tfd.card import Card
from tfd.number import Number
from tfd.test.card_builder import CardBuilder
        
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
        self.assertEqual(card.toString(), "Suit.CLOVERS Number.ACE")

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


from tfd.test.foundation_builder import FoundationBuilder
from tfd.test.card_builder import CardBuilder
from tfd.foundation import Foundation
        
class FoundationTest(unittest.TestCase):

    def test_GivenACompletePile_whenIsCompleteAsked_ReturnTrue(self):
        foundation = FoundationBuilder().cards(13).build()
        self.assertTrue(foundation.isComplete())
        
    def test_GivenAnotCompletePile_whenIsCompleteAsked_ReturnFalse(self):
        foundation = FoundationBuilder().cards(1).build()
        self.assertFalse(foundation.isComplete())

    def test_GivenAemptyFoundation_whenAceofSuitAsksFitsIn_ReturnTrue(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.ACE).build()
        self.assertTrue(foundation.fitsIn(card))
        
    def test_GivenAemptyFoundation_whenAceofOtherSuitAsksFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.CLOVERS).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.ACE).build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenNotemptyFoundation_whenCardMuchBiggerAskFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.FIVE).build()
        self.assertFalse(foundation.fitsIn(card))

    def test_GivenNotemptyFoundation_whenCardOtherSuitAskFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.CLOVERS).number(Number.FOUR).build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenNotemptyFoundation_whenCardthatFitsAskFitsIn_ReturnTrue(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.FOUR).build()
        self.assertTrue(foundation.fitsIn(card))

    def test_GivenemptyFoundation_whenAskEmpty_ReturnTrue(self):
        foundation = FoundationBuilder().build()
        self.assertTrue(foundation.empty())

        
if __name__ == '__main__':
    unittest.main()
                                            
