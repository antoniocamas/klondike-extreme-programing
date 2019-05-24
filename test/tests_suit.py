import unittest
from tfd.suit import Suit
from tfd.color import Color

class SuitTests(unittest.TestCase):

    def test_getColor(self):
        self.assertEqual(Suit.HEARTS.getColor(), Color.RED)


