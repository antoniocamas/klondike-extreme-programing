import unittest
from tfd.exception import InvalidCard
from builders.stock_builder import StockBuilder
from builders.card_builder import CardBuilder

class StockTest(unittest.TestCase):

    def test_GivenAStock_whentakeTopwithLessThanstockSize_ThenReturnXcards(self):
        builder = StockBuilder().cards(4)
        stock = builder.build()
        self.assertEqual(stock.takeTop(1), [builder.getCards()[-1]])
        self.assertEqual(stock.takeTop(2), [builder.getCards()[-2], builder.getCards()[-3]])
        self.assertEqual(stock.takeTop(3), [builder.getCards()[-4]])
        
    def test_GivenAStock_whentakeTopwithMoreThanstockSize_ThenReturnLesscards(self):
        stock = StockBuilder().build()
        self.assertEqual(stock.takeTop(3), [])

    def test_GivenAStock_whenPushFaceUp_ThenException(self):
        waste = StockBuilder().build()
        with self.assertRaises(InvalidCard) as context:
            waste.push(CardBuilder().faceUp().build())
