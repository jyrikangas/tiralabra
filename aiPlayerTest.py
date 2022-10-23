from piece import Piece
from move import Move
import app as app
import aiPlayer as aiPlayer
import unittest

class AiPlayerTest(unittest.TestCase):
    
    def setUp(self) -> None:
        pass
    def test_minimax(self):
        bP = Piece("P", "b", (7,7))
        queen = Piece("Q", "b",(3,3))
        wP = Piece("P", "b", (2,3))
        wK = Piece("K", "b", (1,2))
        board= [[0,0,wK,0,0,0,0,0], [0,0,0,wP,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,queen,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,bP]]
        result = aiPlayer.minimax(board, queen, 1, True)
        result2 = aiPlayer.minimax(board, bP, 1, True)
        breakpoint
        self.assertTrue(result > result2)
        