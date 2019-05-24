import unittest
from builders.waste_builder import WasteBuilder
from builders.card_builder import CardBuilder

class WasteTest(unittest.TestCase):

    def test_GivenAWaste_whenPushFaceDown_ThenCardNotAdded(self):
        waste = WasteBuilder().build()
        waste.push(CardBuilder().build())
        self.assertTrue(waste.empty())
