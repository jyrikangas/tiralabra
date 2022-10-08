from piece import Piece
import app
import unittest
from piece import Piece
import app

class GameTest(unittest.TestCase):
    
    def setUp(self) -> None:
        pass

    def test_knight(self):
        knight = Piece("K", "w",(3,3))
        board= [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,knight,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
        app.knight(knight, board)
        correct= [(4,5),(4,1),(1,2),(2,5),(5,4),(5,2),(4,1),(2,1)]
        wrong = []
        i=0
        j=0
        dontadd=False
        while i<8:
            while j<8:
                for c in correct:
                    if c[0]==i and c[1]==j:
                        dontadd=True
                    if not dontadd:
                        wrong.append((i,j))
                j+=1
            i+=1
        moves = []
        for m in knight.moves:
            moves.append(m.square)
        self.assertTrue(all([item in moves for item in correct]))
        self.assertFalse(any([item in moves for item in wrong]))
        
        

    def test_bishop(self):
        bishop = Piece("B", "w", (3,3))
        board= [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,bishop,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
        app.bishop(bishop, board)
        correct= [(0,0),(1,1),(2,2),(4,4),(5,5),(6,6),(7,7),(4,2),(5,1),(6,0),(2,4),(1,5),(0,6)]
        wrong = []
        i=0
        j=0
        dontadd=False
        while i<8:
            while j<8:
                for c in correct:
                    if c[0]==i and c[1]==j:
                        dontadd=True
                    if not dontadd:
                        wrong.append((i,j))
                j+=1
            i+=1
        moves = []
        for m in bishop.moves:
            moves.append(m.square)
        self.assertTrue(all([item in moves for item in correct]))
        self.assertFalse(any([item in moves for item in wrong]))
        