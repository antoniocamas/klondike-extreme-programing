import unittest
from tfd.test.foundation_builder import FoundationBuilder
from tfd.test.card_builder import CardBuilder
from tfd.foundation import Foundation
from tfd.suit import Suit
from tfd.number import Number
        
class FoundationTest(unittest.TestCase):

    def test_GivenACompletePile_whenIsCompleteAsked_ReturnTrue(self):
        foundation = FoundationBuilder().cards(13).build()
        self.assertTrue(foundation.isComplete())
        
    def test_GivenAnotCompletePile_whenIsCompleteAsked_ReturnFalse(self):
        foundation = FoundationBuilder().cards(1).build()
        self.assertFalse(foundation.isComplete())

    def test_GivenAemptyFoundation_whenAceofSuitAsksFitsIn_ReturnTrue(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.ACE).faceUp().build()
        self.assertTrue(foundation.fitsIn(card))
        
    def test_GivenAemptyFoundation_whenAceofOtherSuitAsksFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.CLOVERS).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.ACE).build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenAemptyFoundation_whenNotAceAsksFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.TWO).faceUp().build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenNotemptyFoundation_whenCardMuchBiggerAskFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.FIVE).faceUp().build()
        self.assertFalse(foundation.fitsIn(card))

    def test_GivenNotemptyFoundation_whenCardOtherSuitAskFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.CLOVERS).number(Number.FOUR).faceUp().build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenNotemptyFoundation_whenCardthatFitsAskFitsIn_ReturnTrue(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.FOUR).faceUp().build()
        self.assertTrue(foundation.fitsIn(card))

    def test_GivenNotemptyFoundation_whenCardFaceDownAskFitsIn_ReturnFalse(self):
        foundation = FoundationBuilder().suit(Suit.PIKES).cards(3).build()
        card = CardBuilder().suit(Suit.PIKES).number(Number.FOUR).build()
        self.assertFalse(foundation.fitsIn(card))
        
    def test_GivenemptyFoundation_whenAskEmpty_ReturnTrue(self):
        foundation = FoundationBuilder().build()
        self.assertTrue(foundation.empty())
