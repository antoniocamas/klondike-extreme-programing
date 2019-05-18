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



