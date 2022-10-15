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

def minimax(board, pieces, depth, maximizingPlayer):
    noMoves = True
    if depth == 0:
        return boardValue(board)
    for piece in pieces:
        legal(piece, board)
        if piece.moves != []:
            noMoves = False
    if noMoves:
        return boardValue(board)
    if maximizingPlayer:
        value = -999999999
        for piece in pieces:
            if piece.side == "b" and piece.alive:
                for move in piece.moves:
                    newboard = copy.deepcopy(board)
                    newboard[piece.position[0]][piece.position[1]] = 0
                    if newboard[move.square[0]][move.square[1]] != 0:
                        newboard[move.square[0]][move.square[1]].die()
                        newboard[move.square[0]][move.square[1]] = 0
                    newboard[move.square[0]][move.square[1]] = piece
                    piece.setPos(move.square)
                    newboard[move.square[0]][move.square[1]] = piece
                    value = max(value, minimax(newboard, copy.deepcopy(pieces), depth - 1, False))
                    print(depth)
        return value
    else:
        value = 999999999
        for piece in pieces:
            if piece.side == "w" and piece.alive:
                for move in piece.moves:
                    newboard = copy.deepcopy(board)
                    newboard[piece.position[0]][piece.position[1]] = 0
                    if newboard[move.square[0]][move.square[1]] != 0:
                        newboard[move.square[0]][move.square[1]].die()
                        newboard[move.square[0]][move.square[1]] = 0
                    newboard[move.square[0]][move.square[1]] = piece
                    piece.setPos(move.square)
                    newboard[move.square[0]][move.square[1]] = piece
                    value = min(value, minimax(newboard, copy.deepcopy(pieces), depth - 1, True))
        return value
    
def chooseMove(boarde, pieces):
    a = True
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            legal(piece, boarde)
            for move in piece.moves:
                
                newboard = copy.deepcopy(boarde)
                newboard[piece.position[0]][piece.position[1]] = 0
                if newboard[move.square[0]][move.square[1]] != 0:
                    newboard[move.square[0]][move.square[1]].die()
                    newboard[move.square[0]][move.square[1]] = 0
                newboard[move.square[0]][move.square[1]] = piece
                piece.setPos(move.square)
                newboard[move.square[0]][move.square[1]] = piece
                move.value = minimax(newboard, copy.deepcopy(pieces), 1, False)
                if a:
                    bestmove = [piece, move]
    
    for piece in pieces:
        if piece.side == "b" and piece.alive:
            for move in piece.moves:
                if bestmove == None:
                    bestmove = [piece, move]
                elif move.value > bestmove[1].value:
                    bestmove = [piece, move]
    return makeMove(boarde, bestmove[0], bestmove[1])
    

def makeMove(boarde, piece, move):
    tox = copy.copy(move.square[0])
    toy = copy.copy(move.square[1])
    fromx = piece.position[0]
    fromy = piece.position[1]
    if boarde[move.square[0]][move.square[1]] != 0:
        boarde[move.square[0]][move.square[1]].die()
        boarde[tox][toy] = 0
    boarde[tox][toy]=piece
    boarde[fromx][fromy]=0
    
    piece.setPos(move.square)
    return boarde
            
            
    
    