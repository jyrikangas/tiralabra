from gamelogic import *
import copy
def evaluate(pieces):
    value = 0
    for piece in pieces:
        if piece.char == "P":
            value += 10
        elif piece.char == "N":
            value += 30
        elif piece.char == "B":
            value += 30
        elif piece.char == "R":
            value += 50
        elif piece.char == "Q":
            value += 90
        elif piece.char == "K":
            value += 900
    return value

def boardValue(board):
    i = 0
    j = 0
    value = 0
    while i < 8:
        while j < 8:
            piece = board[i][j]
            if piece != 0:
                if piece.alive:
                    if piece.side == "b":
                        if piece.char == "P":
                            value += 10
                        elif piece.char == "N":
                            value += 30
                        elif piece.char == "B":
                            value += 30
                        elif piece.char == "R":
                            value += 50
                        elif piece.char == "Q":
                            value += 90
                        elif piece.char == "K":
                            value += 900
                    else:
                        if piece.char == "P":
                            value -= 10
                        elif piece.char == "N":
                            value -= 30
                        elif piece.char == "B":
                            value -= 30
                        elif piece.char == "R":
                            value -= 50
                        elif piece.char == "Q":
                            value -= 90
                        elif piece.char == "K":
                            value -= 900
            j += 1
        i += 1
    return value
##palauttaa listana parametrina annetun puolen nappuloiden siirrot
def moves(pieces, side, board):
    moves = []
    for piece in pieces:
        if side:
            if piece.side == "b":
                for move in piece.moves:
                    moves.append
    
    pass

def minimax(board, pieces, depth, maximizing_player):
    no_moves = True
    if depth == 0:
        return boardValue(board)
    for pieces in board:
        for piece in pieces:
            if piece != 0: 
                legal(piece, board)
                if piece.moves != []:
                    no_moves = False
    if no_moves:
        return boardValue(board)
    if maximizing_player:
        value = -999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "b" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                            value = max(value, minimax(donemove[2], donemove[3], depth - 1, False))
                            print(depth)
        return value
    else:
        value = 999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "w" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                            value = min(value, minimax(donemove[2], donemove[3], depth - 1, True))
        return value
    
def alphabeta(board, pieces, depth, alpha, beta, maximizing_player):
    no_moves = True
    if depth == 0:
        return boardValue(board)
    for pieces in board:
        for piece in pieces:
            if piece != 0: 
                legal(piece, board)
                if piece.moves != []:
                    no_moves = False
    if no_moves:
        return boardValue(board)
    if maximizing_player:
        value = -999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "b" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                            value = max(value, alphabeta(donemove[2], donemove[3], depth - 1, alpha, beta, False))
                            print(depth)
                            if value >= beta:
                                return value
                            a = max(alpha, value)
        return value
    else:
        value = 999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "w" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                            value = min(value, alphabeta(donemove[2], donemove[3], depth - 1, alpha, beta, True))
                            if value <= alpha:
                                return value
                            beta = min(beta, value)
        return value
    
def chooseMove(board, pieces):
    a = True
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            legal(piece, board)
            for move in piece.moves:
                newboard = copy.deepcopy(board)
                donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                move.value = minimax(donemove[2], donemove[3], 2, False)
                if a:
                    bestmove = [piece, move]
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            for move in piece.moves:
                if bestmove is None:
                    bestmove = [piece, move]
                elif move.value > bestmove[1].value:
                    bestmove = [piece, move]
    return bestmove[0], bestmove[1]
    
def chooseMove2(board, pieces):
    a = True
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            legal(piece, board)
            for move in piece.moves:
                newboard = copy.deepcopy(board)
                donemove = doMove(piece, move, newboard, copy.deepcopy(pieces))
                move.value = alphabeta(donemove[2], donemove[3], 2,-999999999, 999999999, False)
                if a:
                    bestmove = [piece, move]
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            for move in piece.moves:
                if bestmove is None:
                    bestmove = [piece, move]
                elif move.value > bestmove[1].value:
                    bestmove = [piece, move]
    return bestmove[0], bestmove[1]

def makeMove(board, piece, move):
    tox = copy.copy(move.square[0])
    toy = copy.copy(move.square[1])
    fromx = piece.position[0]
    fromy = piece.position[1]
    if board[move.square[0]][move.square[1]] != 0:
        board[move.square[0]][move.square[1]].die()
        board[tox][toy] = 0
    board[tox][toy]=piece
    board[fromx][fromy]=0
    
    piece.setPos(move.square)
    return board
            
def doMove(piece, move, board, pieces):
    if board[move.square[0]][move.square[1]] != 0:
        if move.promotion:
            board[move.origin[0]][move.origin[1]].char = "Q"
        ##linnoitus
        elif move.capture.side == piece.side:
            if move.square == (7, 7):
                board[7][6] = board[move.origin[0]][move.origin[1]]
                board[7][6].setPos((7, 6))
                board[move.origin[0]][move.origin[1]] = 0
                board[7][5] = board[move.square[0]][move.square[1]]
                board[7][5].setPos((7, 5))
                board[move.square[0]][move.square[1]] = 0
                
            elif move.square == (7, 0):
                board[7][1] = board[move.origin[0]][move.origin[1]]
                board[7][1].setPos((7, 1))
                board[move.origin[0]][move.origin[1]] = 0
                board[7][2] = board[move.square[0]][move.square[1]]
                board[7][2].setPos((7, 2))
                board[move.square[0]][move.square[1]] = 0
                
            elif move.square == (0, 7):
                board[0][6] = board[move.origin[0]][move.origin[1]]
                board[0][6].setPos((0, 6))
                board[move.origin[0]][move.origin[1]] = 0
                board[0][5] = board[move.square[0]][move.square[1]]
                board[0][5].setPos((0, 5))
                board[move.square[0]][move.square[1]] = 0
                
            elif move.square == (0, 0):
                board[0][1] = board[move.origin[0]][move.origin[1]]
                board[0][1].setPos((0, 1))
                board[move.origin[0]][move.origin[1]] = 0
                board[0][2] = board[move.square[0]][move.square[1]]
                board[0][2].setPos((0, 2))
                board[move.square[0]][move.square[1]] = 0
            return(piece, move, board, pieces)
        else:
            board[move.square[0]][move.square[1]].die
            board[move.square[0]][move.square[1]] = 0
            board[move.square[0]][move.square[1]] = board[move.origin[0]][move.origin[1]]
            board[move.origin[0]][move.origin[1]] = 0
            board[move.square[0]][move.square[1]].setPos(move.square)
            return(piece, move, board, pieces)
    else:
        asdf = board[move.origin[0]][move.origin[1]]
        board[move.square[0]][move.square[1]] = asdf
        board[move.origin[0]][move.origin[1]] = 0
        board[move.square[0]][move.square[1]].setPos(move.square)
        return(piece, move, board, pieces)
    
    