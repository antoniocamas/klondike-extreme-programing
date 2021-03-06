import unittest
from builders.game_builder import GameBuilder
from builders.card_builder import CardBuilder
from helpers.cardstack import CardStackHelper
from helpers.game import GameHelper
from tfd.error import Error
from tfd.suit import Suit
from tfd.number import Number

class GameTest(unittest.TestCase):

    def test_GivenAGameUnfinished_whenAskIsFinished_ThenReturnFalse(self):
        game = GameBuilder().foundationComplete().build()
        self.assertFalse(game.isFinished())

    def test_GivenAGameFinished_whenAskIsFinished_ThenReturnTrue(self):
        game = GameBuilder().finished().build()
        self.assertTrue(game.isFinished())

    def test_GivenAGame_whenClear_ThenTheGameInitialState(self):
        game = GameBuilder().finished().build()
        game.clear()

        gameHelper = GameHelper(game)
        self.assertTrue(gameHelper.areFoundationsInitialState())
        self.assertTrue(gameHelper.arePilesInitialState())
        self.assertTrue(gameHelper.isWasteInInitialState())
        self.assertTrue(gameHelper.isStockInitialState())
        
    def test_GivenAGameWithoutCardInStock_WhenMoveFromStockToWaste_ThenNoCardMoved(self):
        game = GameBuilder().stockEmpty().build()
        self.assertEqual(game.moveFromStockToWaste(), Error.EMPTY_STOCK)

    def test_GivenAGame_WhenmoveFromWasteToFoundationAndFits_ThenTheCardisMoved(self):
        game = GameBuilder().wasteWithAce(Suit.PIKES).build()
        cardTobeMoved = game.getWaste().getTop()
        self.assertIsNone(game.moveFromWasteToFoundation(Suit.PIKES))
        self.assertEqual(game.getFoundations()[Suit.PIKES].getTop(), cardTobeMoved)

    def test_GivenAGame_WhenmoveFromWasteToFoundationAndWasteEmpty_ThenError(self):
        game = GameBuilder().build()
        self.assertEqual(game.moveFromWasteToFoundation(Suit.PIKES), Error.EMPTY_WASTE)

    def test_GivenAGame_WhenmoveFromWasteToFoundationAndDontFit_ThenError(self):
        game = GameBuilder().wasteWithAce(Suit.PIKES).build()
        self.assertEqual(game.moveFromWasteToFoundation(Suit.CLOVERS), Error.NO_FIT_FOUNDATION)

    def test_GivenAGameWithEmptyStock_whenmoveFromWasteToStock_TheCardsAreMoved(self):
        game = GameBuilder().wasteNotEmpty().stockEmpty().build()
        expected_cards = CardStackHelper.fromCardStack(game.getWaste()).flip().reverse().getCards()
        self.assertIsNone(game.moveFromWasteToStock())
        self.assertListEqual(
            CardStackHelper.fromCardStack(game.getStock()).getCards(), expected_cards)
        self.assertTrue(game.getWaste().isEmpty())
        
    def test_GivenAGameWithNotEmptyStock_whenmoveFromWasteToStock_ThenError(self):
        game = GameBuilder().wasteNotEmpty().build()
        self.assertEqual(game.moveFromWasteToStock(), Error.NO_EMPTY_STOCK)

    def test_GivenAGameWithEmptyWaste_whenmoveFromWasteToStock_ThenError(self):
        game = GameBuilder().stockNotEmpty().build()
        self.assertEqual(game.moveFromWasteToStock(), Error.EMPTY_WASTE)

    def test_GivenAGame_WhenMoveFromWasteToPile_ThenCardIsMoved(self):
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.ACE).faceUp().build()
        cardInPile = CardBuilder().suit(Suit.HEARTS).number(Number.TWO).faceUp().build()
        game = GameBuilder().cardInWaste(cardToMove).cardInPile(pileNumber, cardInPile).build()
        self.assertIsNone(game.moveFromWasteToPile(pileNumber))
        self.assertTrue(game.getWaste().isEmpty())
        self.assertEqual(game.getPiles()[pileNumber-1].getTop(), cardToMove)

    def test_GivenAGame_WhenMoveFromWasteToPileThatDontFit_ThenError(self):        
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.ACE).build()
        cardInPile = CardBuilder().suit(Suit.CLOVERS).number(Number.TWO).faceUp().build()
        game = GameBuilder().cardInWaste(cardToMove).cardInPile(pileNumber,cardInPile).build()
        self.assertEquals(game.moveFromWasteToPile(pileNumber), Error.NO_FIT_PILE)
        
    def test_GivenAGameWithEmptyWaste_WhenMoveFromWasteToPile_ThenError(self):
        pileNumber = 1
        game = GameBuilder().build()
        self.assertEquals(game.moveFromWasteToPile(pileNumber), Error.EMPTY_WASTE)

    def test_GivenAGame_WhenMoveFromPileToFoundation_ThenCardIsMoved(self):
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.ACE).faceUp().build()
        game = GameBuilder()\
               .cardInPile(pileNumber, CardBuilder().faceUp().build())\
               .cardInPile(pileNumber, cardToMove)\
               .build()
        self.assertIsNone(game.moveFromPileToFoundation(pileNumber, Suit.PIKES))
        self.assertNotEqual(game.getPiles()[pileNumber-1].getTop(), cardToMove)
        self.assertEqual(game.getFoundations()[Suit.PIKES].getTop(), cardToMove)
        self.assertTrue(game.getPiles()[pileNumber-1].getTop().isFaceUp())        
                
    def test_GivenAGameWithEmptyPile_WhenMoveFromPileToFoundation_ThenError(self):
        pileNumber = 1
        game = GameBuilder().pileEmpty(pileNumber).build()
        self.assertEqual(game.moveFromPileToFoundation(pileNumber, Suit.PIKES), Error.EMPTY_PILE)

    def test_GivenAGame_WhenMoveFromPileToFoundation_ThenError(self):
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.ACE).faceUp().build()
        game = GameBuilder()\
               .cardInPile(pileNumber, CardBuilder().faceUp().build())\
               .cardInPile(pileNumber, cardToMove)\
               .build()
        self.assertEqual(
            game.moveFromPileToFoundation(pileNumber, Suit.HEARTS), Error.NO_FIT_FOUNDATION)

    def test_GivenAGame_WhenMoveFromFoundationToPile_ThenCardIsMoved(self):
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.KING).faceUp().build()
        cardLeft = CardBuilder().suit(Suit.PIKES).number(Number.QUEEN).faceUp().build()
        game = GameBuilder().pileEmpty(pileNumber).foundationComplete(Suit.PIKES).build()
        self.assertIsNone(game.moveFromFoundationToPile(Suit.PIKES, pileNumber))
        self.assertEqual(game.getPiles()[pileNumber-1].getTop(), cardToMove)
        self.assertEqual(game.getFoundations()[Suit.PIKES].getTop(), cardLeft)

    def test_GivenAEmptyFoundation_WhenMoveFromFoundationToPile_ThenError(self):
        pileNumber = 1
        game = GameBuilder().foundationEmpty(Suit.PIKES).build()
        self.assertEqual(
            game.moveFromFoundationToPile(Suit.PIKES, pileNumber), Error.EMPTY_FOUNDATION)

    def test_GivenAMoveThatDontFit_WhenMoveFromFoundationToPile_ThenError(self):
        pileNumber = 1
        cardToMove = CardBuilder().suit(Suit.PIKES).number(Number.QUEEN).faceUp().build()
        game = GameBuilder().pileEmpty(pileNumber).foundationComplete(Suit.PIKES).build()
        game.moveFromFoundationToPile(Suit.PIKES, pileNumber)
        self.assertEqual(game.moveFromFoundationToPile(Suit.PIKES, pileNumber), Error.NO_FIT_PILE)

    def test_GivenAMoveThatFits_WhenMoveFromPileToPile_ThenCardsMove(self):
        pileNumberOrigin = 1
        pileNumberDest = 7
        nCardsMoved = 4
        game = GameBuilder().pileWithFaceUpCards(pileNumberOrigin).pileEmpty(pileNumberDest).build()
        cardsInPile = CardStackHelper.fromCardStack(game.getPiles()[pileNumberOrigin-1]).getCards()
        self.assertIsNone(game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved))
        self.assertListEqual(
            CardStackHelper.fromCardStack(game.getPiles()[pileNumberDest-1]).getCards(),
            cardsInPile[len(cardsInPile)-nCardsMoved:])
        
    def test_GivenAMoveThatFits_WhenMoveFromPileToPile_ThenCardOriginFlipped(self):
        pileNumberOrigin = 1
        pileNumberDest = 7
        nCardsMoved = 4
        game = GameBuilder().pileWithFaceUpCards(pileNumberOrigin).pileEmpty(pileNumberDest).build()
        cardsInPile = CardStackHelper.fromCardStack(game.getPiles()[pileNumberOrigin-1]).getCards()
        self.assertIsNone(game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved))
        cardsInPile[0].flip()
        self.assertEqual(game.getPiles()[pileNumberOrigin-1].getTop(), cardsInPile[0])
        
    def test_GivenAMoveThatDontFit_WhenMoveFromPileToPile_ThenError(self):
        pileNumberOrigin = 1
        pileNumberDest = 7
        nCardsMoved = 3
        game = GameBuilder()\
               .pileWithFaceUpCards(pileNumberOrigin)\
               .cardInPile(pileNumberDest, CardBuilder().number(Number.ACE).faceUp().build()).build()
        self.assertEqual(
            game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved),
            Error.NO_FIT_PILE
        )
        
    def test_GivenAMoveWithToManyCards_WhenMoveFromPileToPile_ThenError(self):
        pileNumberOrigin = 1
        pileNumberDest = 7
        nCardsMoved = 5
        game = GameBuilder()\
               .pileWithFaceUpCards(pileNumberOrigin)\
               .cardInPile(pileNumberDest, CardBuilder().number(Number.ACE).faceUp().build()).build()
        self.assertEqual(
            game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved),
            Error.NO_ENOUGH_CARDS_PILE
        )

    def test_GivenAMove_WhenMoveFromPileToSamePile_ThenError(self):
        pileNumberOrigin = 1
        pileNumberDest = 1
        nCardsMoved = 1
        game = GameBuilder()\
               .pileWithFaceUpCards(pileNumberOrigin)\
               .cardInPile(pileNumberDest, CardBuilder().number(Number.ACE).faceUp().build()).build()
        self.assertEqual(
            game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved),
            Error.SAME_PILE
        )

    def test_GivenAMove_WhenMoveFromEmptyPileToPile_ThenError(self):
        pileNumberOrigin = 1
        pileNumberDest = 7
        nCardsMoved = 1
        game = GameBuilder().pileEmpty(pileNumberOrigin).build()
        self.assertEqual(
            game.moveFromPileToPile(pileNumberOrigin, pileNumberDest, nCardsMoved),
            Error.EMPTY_PILE
        )



