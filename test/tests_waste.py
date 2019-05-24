import unittest
from tfd.exception import InvalidCard
from builders.waste_builder import WasteBuilder
from builders.card_builder import CardBuilder

class WasteTest(unittest.TestCase):

    def test_GivenAWaste_whenPushFaceDown_ThenException(self):
        waste = WasteBuilder().build()
        with self.assertRaises(InvalidCard) as context:
            waste.push(CardBuilder().build())
