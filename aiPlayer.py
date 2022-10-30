from gamelogic import *
import copy

def boardValue(board):
    i = 0
    j = 0
    value = 0
    while i < 8:
        while j < 8:
            piece = board[i][j]
            if piece != 0:
                if piece.side == 'b':
                    if piece.char == 'P':
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
                
                elif piece.side == "w":
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
        j = 0
        i += 1

    return value


def alphabeta(board, depth, alpha, beta, maximizing_player):
    no_moves = True
    game_over = False
    king1 = False
    king2 = False
    if depth == 0:
        return boardValue(board)
    for pieces in board:
        for piece in pieces:
            if piece != 0:
                legal(piece, board)
                if piece.cantmove:
                    piece.moves = []
                if piece.moves != []:
                    no_moves = False
                if piece.char == "K" and piece.side=="w":
                    king1 = True
                elif piece.char == "K" and piece.side=="b":
                    king2 = True
    if no_moves or (not king1 or not king2):
        return boardValue(board)

    if maximizing_player:
        value = -999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "b" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard)
                            
                            evalu = alphabeta(donemove[2], depth - 1, alpha, beta, False)
                            value = max(value, evalu)
                            alpha = max(alpha, evalu)
                            if beta <= alpha:
                                break
                if beta <= alpha:
                    break 
            if beta <= alpha:
                break                
        return value
    else:
        value = 999999999
        for pieces in board:
            for piece in pieces:
                if piece != 0:
                    if piece.side == "w" and piece.alive:
                        for move in piece.moves:
                            newboard = copy.deepcopy(board)
                            donemove = doMove(piece, move, newboard)
                            evalu = alphabeta(donemove[2], depth - 1, alpha, beta, True)
                            value = min(value, evalu)
                            beta = min(beta, evalu)
                            if beta <= alpha:
                               break
                if beta <= alpha:
                    break
            if beta <= alpha:
               break
         
        return value

##laskee parhaan siirron ja palauttaa nappulan jota siirretään ja siirron joka tehdään
def chooseMove2(board):
    a = True
    
    for pieces in board:
        for piece in pieces:
            if piece != 0:
                if piece.side == "b" and piece.alive:
                    legal(piece, board)
                    for move in piece.moves:
                        newboard = copy.deepcopy(board)
                        donemove = doMove(copy.deepcopy(piece), move, newboard)
                        move.setValue(alphabeta(donemove[2], 2,-999999999, 999999999, False))

                        if a:
                            bestmove = [piece, move]
                            a = False
    
    for pieces in board:
        for piece in pieces:
            if piece != 0:
                if piece.side == "b" and piece.alive:
                    for move in piece.moves:
                        if bestmove is None:
                            bestmove = [piece, move]
                        elif move.value > bestmove[1].value:
                            bestmove = [piece, move]
    return bestmove[0], bestmove[1]


def doMove(piece, move, board):
    if board[move.square[0]][move.square[1]] != 0:
        if move.promotion:
            board[move.origin[0]][move.origin[1]].char = "Q"
            return(piece, move, board)
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
            return(piece, move, board)
        else:
            board[move.square[0]][move.square[1]].die()
            board[move.square[0]][move.square[1]] = 0
            board[move.square[0]][move.square[1]] = board[move.origin[0]][move.origin[1]]
            board[move.origin[0]][move.origin[1]] = 0
            board[move.square[0]][move.square[1]].setPos(move.square)
            return(piece, move, board)
    else:
        asdf = board[move.origin[0]][move.origin[1]]
        board[move.square[0]][move.square[1]] = asdf
        board[move.origin[0]][move.origin[1]] = 0
        board[move.square[0]][move.square[1]].setPos(move.square)
        return(piece, move, board)
    
    