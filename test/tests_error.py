import unittest
from tfd.error import Error

class ErrorTests(unittest.TestCase):

    def test_GivenAnError_WhenGetMessage_ThenMessageIsGotten(self):
        self.assertEqual(Error.SAME_PILE.getMessage(), "It is the same Pile")
