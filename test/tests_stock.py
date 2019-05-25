import unittest
from tfd.exception import InvalidCard
from builders.stock_builder import StockBuilder
from builders.card_builder import CardBuilder

class StockTest(unittest.TestCase):

    def test_GivenAStock_whentakeTopwithLessThanstockSize_ThenReturnXcards(self):
        builder = StockBuilder().cards(4)
        stock = builder.build()
        self.assertEqual(stock.getTopCards(1), [builder.getCards()[-1]])
        self.assertEqual(stock.getTopCards(2), [x for x in reversed(builder.getCards()[2:])])
        self.assertEqual(stock.getTopCards(3), [x for x in reversed(builder.getCards()[1:])])
        self.assertEqual(stock.getTopCards(4), [x for x in reversed(builder.getCards()[:])])
        stock.removeTopCards(4)
        
    def test_GivenAStock_whentakeTopwithMoreThanstockSize_ThenReturnLesscards(self):
        stock = StockBuilder().build()
        self.assertEqual(stock.getTopCards(3), [])

    def test_GivenAStock_whenPushFaceUp_ThenException(self):
        stock = StockBuilder().build()
        with self.assertRaises(InvalidCard) as context:
            stock.push(CardBuilder().faceUp().build())

    def test_GivenAStock_whenremoveTopCards_ThenXcardsRemoved(self):
        builder = StockBuilder().cards(4)
        stock = builder.build()
        stock.removeTopCards(1)
        self.assertEqual(stock.getTopCards(1), [builder.getCards()[-2]])
        stock.removeTopCards(1)
        self.assertEqual(stock.getTopCards(1), [builder.getCards()[-3]])
        stock.removeTopCards(2)
        self.assertTrue(stock.empty())

