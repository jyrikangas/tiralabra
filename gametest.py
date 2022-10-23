from piece import Piece
import app as app
import unittest
import aiPlayer as aiPlayer
import copy
class GameTest(unittest.TestCase):
    
    def setUp(self) -> None:
        pass

    def test_knight(self):
        knight = Piece("N", "w",(3,3))
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
        board = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
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
        
    def test_minimax(self):
        bP = Piece("P", "b", (7,7))
        queen = Piece("Q", "b",(1,1))
        queen1 = Piece("Q", "b",(1,5))
        wP = Piece("P", "w", (1,3))
        wK = Piece("K", "w", (1,2))
        pieces = [bP, queen, wP, wK]
        pieces1 = [bP, queen1, wP, wK]
        board = [[0,queen,wK,wP,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,bP]]
        board1 = [[0,0,wK,wP,0,queen1,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,bP]]
        result = aiPlayer.minimax(board, pieces, 2, False)
        result2 = aiPlayer.minimax(board1, pieces1, 2, False)
        self.assertTrue(result < result2)
    
    def test_ai_chooses_highest_value_move_2(self):
        b_pawn = Piece("P", "b", (3, 4))
        b_pawn2 = Piece("P", "b", (3, 3))
        w_pawn = Piece("P", "w", (2, 5))
        w_king = Piece("K", "w", (2, 2))
        
        board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, w_king, 0, 0, w_pawn, 0, 0], [0, 0, 0, b_pawn2, b_pawn, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        result = aiPlayer.chooseMove(board, [w_pawn, w_king, b_pawn, b_pawn2])
        self.assertTrue(result[1].square == (2, 2))
        
    def test_ai_chooses_highest_value_move(self):
        queen = Piece("Q", "b", (3, 3))
        w_pawn = Piece("P", "w", (3, 7))
        w_king = Piece("K", "w", (0, 3))
        w_queen = Piece("Q", "w", (3, 0))
        
        board = [[0, 0, 0, w_king, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [w_queen, 0, 0, queen, 0, 0, 0, w_pawn],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        result = aiPlayer.chooseMove(board, [queen, w_pawn, w_king, w_queen])
        self.assertTrue(result[1].square == (0, 3))
        
    def test_ai_castles(self):
        king = Piece("K", "b", (7, 4))
        rook = Piece("R", "b", (7, 7))
        board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, king, 0, 0, rook]]
        result = aiPlayer.chooseMove(board, [king, rook])
        self.assertTrue(result[1].square == (7, 7))

    def test_ai_promotes(self):
        pawn = Piece("P", "b", (0, 0))
        board = [[pawn, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        result = aiPlayer.chooseMove(board, [pawn])
        self.assertTrue(result[1].promotion)
        
    def test_alpha_beta(self):
        white_rook = Piece("R", "w", (0, 0))
        white_knight = Piece("N", "w", (0, 1))
        white_bishop = Piece("B", "w", (0, 2))
        white_queen = Piece("Q", "w", (0, 3))
        white_king = Piece("K", "w", (0, 4))
        white_bishop2 = Piece("B", "w", (0, 5))
        white_knight2 = Piece("N", "w",(0,6))
        white_rook_2 = Piece("R", "w",(0,7))
        white_pawn_1 = Piece("P","w",(1,0))
        white_pawn_2 = Piece("P","w",(1,1))
        white_pawn_3 = Piece("P","w",(1,2))
        white_pawn_4 = Piece("P","w",(1,3))
        white_pawn_5 = Piece("P","w",(1,4))
        white_pawn_6 = Piece("P","w",(1,5))
        white_pawn_7 = Piece("P","w",(1,6))
        white_pawn_8 = Piece("P","w",(1,7))

        bR = Piece("R", "b",(7,0))
        bN = Piece("N", "b",(7,1))
        bB = Piece("B", "b",(7,2))
        bQ = Piece("Q", "b",(7,3))
        bK = Piece("K", "b",(7,4))
        bB2 = Piece("B", "b",(7,5))
        bN2 = Piece("N", "b",(7,6))
        bR2 = Piece("R", "b",(7,7))
        bP1 = Piece("P","b",(6,0))
        bP2 = Piece("P","b",(6,1))
        bP3 = Piece("P","b",(6,2))
        bP4 = Piece("P","b",(6,3))
        bP5 = Piece("P","b",(6,4))
        bP6 = Piece("P","b",(6,5))
        bP7 = Piece("P","b",(6,6))
        bP8 = Piece("P","b",(6,7))

        ##listat molempien pelaajien nappuloista
        whitepieces = (white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop2,white_knight2,white_rook_2, white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8)
        blackpieces = (bR,bN,bB,bQ,bK,bB2,bN2,bR2, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8)
        pieces = [white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop2,white_knight2,white_rook_2, white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8, bR,bN,bB,bQ,bK,bB2,bN2,bR2, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8]
        ##pelilauta
        board = [[white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop2,white_knight2,white_rook_2], [white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8],
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
        [bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8], [bR,bN,bB,bQ,bK,bB2,bN2,bR2]]
        res1 = aiPlayer.chooseMove(copy.deepcopy(board), copy.deepcopy(pieces))
        res2 = aiPlayer.chooseMove2(copy.deepcopy(board), copy.deepcopy(pieces))
        self.assertTrue(res1 == res2)