from move import Move
from piece import Piece
##pylint: disable=too-many-function-args
def validmoves(pieces, board):
    moves = []
    for piece in pieces:
        legal(piece, board)
       ##print(piece.char + "@" +str(piece.position))
       ##print(piece.moves)
    
    return 
    
##käy läpi kohdat joihin nappula voi siirtyä ja palauttaa listat ruuduista joihin nappulan voi siirtää ja joihin se voi siirtyä mutta joissa on vastustajan nappula.
def legal(piece, board):
    piece.moves = []
    if piece.char == "P":
        if piece.side == "w":
            ## jos sotilas on aloitusruudussa, se voi siirtyä kahteen edessä olevaan ruutuun, jos ne ovat tyhjiä
            if piece.position[0] == 1:
                if board[2][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position[0], piece.position[1]), (2, piece.position[1]), board[2][piece.position[1]]))
                if board[3][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position[0], piece.position[1]), (3, piece.position[1]), board[3][piece.position[1]]))
            
            if piece.position[0] < 7:
                ## jos edessä oleva ruutu on tyhjä, sotilas voi liikkua eteenpäin
                if board[piece.position[0] + 1][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position[0], piece.position[1]), (piece.position[0] + 1, piece.position[1]), board[piece.position[0]+1][piece.position[1]]))
                ## nämä rivit tarkastavat onko nappula laudan reunalla, ja jos laudalla olevalla etuviistossa sijaitsevalla ruudulla on vastapuolen nappula, se voidaan lisätä siirtolistaan.
                if piece.position[1] < 7:
                    if board[piece.position[0] + 1][piece.position[1] + 1] != 0:
                        if board[piece.position[0] + 1][piece.position[1]+1].side == "b":
                            piece.moves.append(Move((piece.position[0], piece.position[1]), (piece.position[0] + 1,piece.position[1] + 1), board[piece.position[0] + 1][piece.position[1] + 1]))
                if piece.position[1] > 0:
                    if board[piece.position[0] + 1][piece.position[1] - 1] != 0:
                        if board[piece.position[0] + 1][piece.position[1] - 1].side == "b":
                            piece.moves.append(Move((piece.position[0], piece.position[1]), (piece.position[0] + 1, piece.position[1] - 1), board[piece.position[0] + 1][piece.position[1] - 1]))
                ##ylennys
            if piece.position[0] == 7:
                piece.moves.append(Move.makePromotion((piece.position),(piece.position), piece, True))
                    
            
        else:
            ## jos sotilas (musta) on aloitusruudussa, se voi siirtyä kahteen edessä olevaan ruutuun, jos ne ovat tyhjiä
            if piece.position[0] == 6:
                if board[5][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position[0], piece.position[1]), (5, piece.position[1]), board[5][piece.position[1]]))
                if board[4][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position), (4, piece.position[1]), board[4][piece.position[1]]))
            ## jos edessä oleva ruutu on pelilaudalla ja tyhjä, sotilas voi liikkua eteenpäin
            if piece.position[0] > 0:
                if board[piece.position[0] - 1][piece.position[1]] == 0:
                    piece.moves.append(Move((piece.position), (piece.position[0] - 1, piece.position[1]), board[piece.position[0] - 1][piece.position[1]]))
                ## nämä rivit tarkastavat onko nappula laudan reunalla, ja jos laudalla olevalla etuviistossa sijaitsevalla ruudulla on vastapuolen nappula, se voidaan lisätä siirtolistaan.
                if piece.position[1] < 7:
                    if board[piece.position[0] - 1][piece.position[1] + 1] != 0:
                        if board[piece.position[0] - 1][piece.position[1] + 1].side == "w":
                            piece.moves.append(Move((piece.position), (piece.position[0] - 1, piece.position[1] + 1), board[piece.position[0] - 1][piece.position[1] + 1]))
                if piece.position[1] > 0:
                    if board[piece.position[0] - 1][piece.position[1] - 1] != 0:
                        if board[piece.position[0] - 1][piece.position[1] - 1].side == "w":
                            piece.moves.append(Move((piece.position), (piece.position[0] - 1,piece.position[1] - 1), board[piece.position[0] - 1][piece.position[1] - 1]))
            if piece.position[0] == 0:
               piece.moves.append(Move.makePromotion((piece.position), (piece.position), piece, True))

    if piece.char == "R":
        rook(piece, board)
    if piece.char == "N":
        knight(piece, board)
    if piece.char == "B":
        bishop(piece, board)
    if piece.char == "Q":
        rook(piece, board)
        bishop(piece, board)
    if piece.char == "K":
        king(piece, board)
    return 

def king(piece, board):
    ##castling/linnoitus
    if piece.hasNotMoved:
        if piece.side == "w":
            if board[0][0] != 0:
                if board[0][0].hasNotMoved:
                    if board[0][1] == 0 and board[0][2] == 0 and board [0][3] == 0:
                        piece.moves.append(Move((piece.position), (0,0), board[0][0]))
            if board[0][7] != 0:
                if board[0][7].hasNotMoved:
                    if board[0][5] == 0 and board[0][6] == 0:
                        piece.moves.append(Move((piece.position), (0,7), board[0][7]))
        else:
            if board[7][0] != 0:
                if board[7][0].hasNotMoved:
                    if board[7][1] == 0 and board[7][2] == 0 and board [7][3] == 0:
                        piece.moves.append(Move((piece.position), (7,0), board[7][0]))
            if board[7][7] != 0:
                if board[7][7].hasNotMoved:
                    if board[7][5] == 0 and board[7][6] == 0:
                        piece.moves.append(Move((piece.position), (7,7), board[7][7]))
    x = max(piece.position[0] - 1, 0)
    y = max(piece.position[1] - 1, 0)
    xend = min(piece.position[0] + 1, 7)
    yend = min(piece.position[1] + 1, 7)
    while(x <= xend):
        while(y <= yend):
            if board[x][y] == 0:
                piece.moves.append(Move((piece.position), (x, y), board[x][y]))
                y += 1
            elif board[x][y].side != piece.side:
                piece.moves.append(Move((piece.position), (x, y), board[x][y]))
                y += 1
            else:
                y += 1
        x += 1
    return

def rook(piece, board):
    
    x = piece.position[0]
    y = piece.position[1] + 1
    ##käy läpi ruudut samassa sarakkeessa nappulan yläpuolella
    while y < 8:
        if board[piece.position[0]][y] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0], y), board[piece.position[0]][y]))
            y+=1
        elif board[piece.position[0]][y].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0],y), board[piece.position[0]][y]))
            y = 9  
        else:
            y=9  
            
    x = piece.position[0] + 1
    y = piece.position[1]
    ##käy läpi rivin ruudut nappulan oikealla puolella 
    while x < 8:
        if board[x][piece.position[1]] == 0:
            piece.moves.append(Move((piece.position), (x, piece.position[1]), board[x][piece.position[1]]))
            x += 1
        elif board[x][piece.position[1]].side != piece.side:
            piece.moves.append(Move((piece.position), (x, piece.position[1]),board[x][piece.position[1]]))
            x=8            
        else:
            x=8 
    
    
    x = piece.position[0]
    y = piece.position[1] - 1
    ##käy läpi sarakkeen ruudut nappulan alapuolelta
    while y >= 0:
        if board[piece.position[0]][y] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0], y), board[piece.position[0]][y]))
            y -=1 
        elif board[piece.position[0]][y].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0], y), board[piece.position[0]][y]))
            y=-1  
        else:
            y=-1
    x = piece.position[0] - 1
    y = piece.position[1] 
    ##rivin ruudut nappulan vasemmalta
    while x >= 0:
        if board[x][piece.position[1]] == 0:
            piece.moves.append(Move((piece.position), (x, piece.position[1]), board[x][piece.position[1]]))
            x-=1
        elif board[x][piece.position[1]].side != piece.side:
            piece.moves.append(Move((piece.position), (x, piece.position[1]), board[x][piece.position[1]]))
            x=-1            
        else:
            x=-1
    return

def bishop(piece, board):
    x = piece.position[0]+1
    y = piece.position[1]+1
    while(x<8 and y<8):
        if board[x][y]==0:
            piece.moves.append(Move((piece.position), (x, y), board[x][y]))
            x+=1
            y+=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x=9
        else:
            x=9
    x=piece.position[0]-1
    y=piece.position[1]-1
    while(x>=0 and y>=0):
        if board[x][y]==0:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x-=1
            y-=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x=-1
        else:
            x=-1

    x=piece.position[0]+1
    y=piece.position[1]-1
    while(x<8 and y>=0):
        if board[x][y]==0:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x+=1
            y-=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x=9
        else:
            x=9

    x = piece.position[0]-1
    y = piece.position[1]+1
    while(x>=0 and y<8):
        if board[x][y]==0:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x-=1
            y+=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((piece.position), (x,y),board[x][y]))
            x=-1
        else:
            x=-1
    return

def knight(piece, board):
    top = 7 - piece.position[0]
    bot = piece.position[0]
    right = 7 - piece.position[1]
    left = piece.position[1]
    if top >= 2 and right >= 1:
        if board[piece.position[0] +2][piece.position[1] + 1] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0]+2,piece.position[1]+1), board[piece.position[0]+2][piece.position[1]+1]))
        elif board[piece.position[0]+2][piece.position[1]+1].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0] + 2, piece.position[1] + 1), board[piece.position[0] + 2][piece.position[1] + 1]))
    if top >= 2 and left >= 1:
        if board[piece.position[0]+2][piece.position[1]-1] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0]+2,piece.position[1]-1), board[piece.position[0]+2][piece.position[1]-1]))
        elif board[piece.position[0]+2][piece.position[1]-1].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0]+2,piece.position[1]-1), board[piece.position[0]+2][piece.position[1]-1]))
        
    if top >= 1 and right >= 2:
        if board[piece.position[0]+1][piece.position[1]+2] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0]+1,piece.position[1]+2), board[piece.position[0]+1][piece.position[1]+2]))
        elif board[piece.position[0]+1][piece.position[1]+2].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0]+1,piece.position[1]+2), board[piece.position[0]+1][piece.position[1]+2]))
    if top >= 1 and left >= 2:
        if board[piece.position[0]+1][piece.position[1]-2] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0]+1,piece.position[1]-2), board[piece.position[0]+1][piece.position[1]-2]))
        elif board[piece.position[0]+1][piece.position[1]-2].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0]+1,piece.position[1]-2), board[piece.position[0]+1][piece.position[1]-2]))
    
    if bot >= 2 and right >= 1:
        if board[piece.position[0]-2][piece.position[1]+1] ==0:
            piece.moves.append(Move((piece.position), (piece.position[0]-2,piece.position[1]+1), board[piece.position[0]-2][piece.position[1]+1]))
        elif board[piece.position[0]-2][piece.position[1]+1].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0]-2,piece.position[1]+1), board[piece.position[0]-2][piece.position[1]+1]))
    if bot >= 2 and left >= 1:
        if board[piece.position[0]-2][piece.position[1]-1] ==0:
            piece.moves.append(Move((piece.position), (piece.position[0]-2,piece.position[1]-1), board[piece.position[0]-2][piece.position[1]-1]))
        elif board[piece.position[0]-2][piece.position[1]-1].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0]-2,piece.position[1]-1), board[piece.position[0]-2][piece.position[1]-1]))
        
    if bot >= 1 and right >= 2:
        if board[piece.position[0] - 1][piece.position[1] + 2] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0] - 1, piece.position[1] + 2), board[piece.position[0] - 1][piece.position[1] + 2]))
        elif board[piece.position[0] - 1][piece.position[1] + 2].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0] - 1, piece.position[1] + 2), board[piece.position[0] - 1][piece.position[1] + 2]))
    if bot >= 1 and left >= 2:
        if board[piece.position[0] - 1][piece.position[1] - 2] == 0:
            piece.moves.append(Move((piece.position), (piece.position[0] - 1,piece.position[1] - 2), board[piece.position[0] - 1][piece.position[1] - 2]))
        elif board[piece.position[0] - 1][piece.position[1] - 2].side != piece.side:
            piece.moves.append(Move((piece.position), (piece.position[0] -1 , piece.position[1] - 2), board[piece.position[0] - 1][piece.position[1] - 2]))
    return
##ottaa käyttäjän valinnan siitä miksi nappulaksi sotilas ylennetään ja toteuttaa ylennyksen
def promotion(piece, board):
    while True:
        choice = input("valitse Q (kuningatar), R (torni), N(ratsu), tai B (lähetti):")
        if choice == "Q":
            piece.char = "Q"
            return
        elif choice == "R":
            piece.char = "R"
            return
        elif choice == "N":
            piece.char = "N"
            return
        elif choice == "B":
            piece.char = "B"
            return
