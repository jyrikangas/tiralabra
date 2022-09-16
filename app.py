##pylint: disable=too-many-function-args

import pygame
from piece import Piece
##pelilaudan alustus. w=valkoinen, b=musta, R=torni, N=ratsu, B=lähetti, Q=kuningatar, K=kuningas, P=sotilas

wR = Piece("R", "w",(0,0))
wN = Piece("N", "w",(0,1))
wB = Piece("B", "w",(0,2))
wQ = Piece("Q", "w",(0,3))
wK = Piece("K", "w",(0,4))
wB2 = Piece("B", "w",(0,5))
wN2 = Piece("N", "w",(0,6))
wR2 = Piece("R", "w",(0,7))
wP1 = Piece("P","w",(1,0))
wP2 = Piece("P","w",(1,1))
wP3 = Piece("P","w",(1,2))
wP4 = Piece("P","w",(1,3))
wP5 = Piece("P","w",(1,4))
wP6 = Piece("P","w",(1,5))
wP7 = Piece("P","w",(1,6))
wP8 = Piece("P","w",(1,7))


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
whitepieces = (wR,wN,wB,wQ,wK,wB2,wN2,wR2, wP1,wP2,wP3,wP4,wP5,wP6,wP7,wP8)
blackpieces = (bR,bN,bB,bQ,bK,bB2,bN,bR, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8)
##pelilauta
board = [(wR,wN,wB,wQ,wK,wB,wN,wR), (wP1,wP2,wP3,wP4,wP5,wP6,wP7,wP8), 
(0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0), 
(0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0), 
(bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8), (bR,bN,bB,bQ,bK,bB2,bN2,bR2)]
print(board)

##käy palauttaa listan laillisista siirroista ja vastustajan nappuloista jotka voi ottaa. listat eivät sisällä päällekkäisyyksiä.
#  palautus muotota [([nappulan siirrot], [vihollisen nappulat jotka nappulalla voi ottaa]), (sama seuraavalle nappulalle )...]
def validmoves(pieces):
    moves = []
    for piece in pieces:
        moves.append(legal(piece))
    return moves
    
##käy läpi kohdat joihin nappula voi siirtyä ja palauttaa listat ruuduista joihin nappulan voi siirtää ja joihin se voi siirtyä mutta joissa on vastustajan nappula.
def legal(piece):
    moves = []
    captures = []
    if piece.char == "P":
        if piece.side == "w":
            if piece.position[0]==1:
                if board[2][piece.position[1]]==0:
                    moves.append((2,piece.position[1]))
                if board[3][piece.position[1]]==0:
                    moves.append((3,piece.position[1]))
            
            if piece.position[0]<7:
                if board[piece.position[0]+1][piece.position[1]] ==0:
                    moves.append((piece.position[0]+1,piece.position[1]))
                elif board[piece.position[0]+1][piece.position[1]].side != piece.side:
                    captures.append((piece.position[0]+1,piece.position[1]))
                if piece.position[1]<7:
                    if board[piece.position[0]+1][piece.position[1]+1]!=0:
                        if board[piece.position[0]+1][piece.position[1]+1].side=="b":
                            captures.append((piece.position[0]+1,piece.position[1]+1))
                if piece.position[1]>0:
                    if board[piece.position[0]+1][piece.position[1]-1]!=0:
                        if board[piece.position[0]+1][piece.position[1]-1].side=="b":
                            captures.append((piece.position[0]+1,piece.position[1]-1))
            
        else:
            if piece.position[0]==6:
                if board[5][piece.position[1]]==0:
                    moves.append((5,piece.position[1]))
                if board[4][piece.position[1]]==0:
                    moves.append((4,piece.position[1]))
            
            if piece.position[0]<0:
                if board[piece.position[0]-1][piece.position[1]]==0:
                    moves.append(piece.position[0]-1,piece.position[1])
                elif board[piece.position[0]-1][piece.position[1]].side != piece.side:
                    captures.append((piece.position[0]-1,piece.position[1]))
                if piece.position[1]<7:
                    if board[piece.position[0]-1][piece.position[1]+1]!=0:
                        if board[piece.position[0]-1][piece.position[1]+1].side=="w":
                            captures.append((piece.position[0]-1,piece.position[1]+1))
                if piece.position[1]>0:
                    if board[piece.position[0]-1][piece.position[1]-1]!=0:
                        if board[piece.position[0]-1][piece.position[1]-1].side=="w":
                            captures.append((piece.position[0]-1,piece.position[1]-1))

    if piece.char == "R":
        rook(piece, moves, captures)
    if piece.char == "N":
        knight(piece, moves, captures)
    if piece.char == "B":
        bishop(piece,moves,captures)
    if piece.char == "Q":
        rook(piece,moves,captures)
        bishop(piece,moves,captures)
    if piece.char == "K":
        x =max(piece.position[0]-1,0)
        y =max(piece.position[1]-1,0)
        xend = min(piece.position[0]+1,7)
        yend = min(piece.position[1]+1,7)
        while(x<=xend):
            while(y<=yend):
                if board[x][y]==0:
                    moves.append((x,y))
                    y+=1
                elif board[x][y].side!=piece.side:
                    captures.append((x,y))
                    y+=1
                else:
                    y+=1
            x+=1
    return (moves, captures)
    

def rook(piece,moves,captures):
    x=piece.position[0]
    y=piece.position[1]
    while y<8:
        if board[piece.position[0]][y]==0:
            moves.append((piece.position[0],y))
            y+=1
        elif board[piece.position[0]][y].side!=piece.side:
            captures.append((piece.position[0],y))
            y=9  
        else:
            y=9  
    while x<8:
        if board[x][piece.position[1]]==0:
            moves.append((x,piece.position[1]))
            x+=1
        elif board[x][piece.position[1]].side!=piece.side:
            captures.append((x,piece.position[1]))
            x=8            
        else:
            x=8 
    
    
    x=piece.position[0]
    y=piece.position[1]
    while y>=0:
        if board[piece.position[0]][y]==0:
            moves.append((piece.position[0],y))
            y-=1
        elif board[piece.position[0]][y].side!=piece.side:
            captures.append((piece.position[0],y))
            y=-1  
        else:
            y=-1  
        while x>=0:
            if board[x][piece.position[1]]==0:
                moves.append((x,piece.position[1]))
                x-=1
            elif board[x][piece.position[1]].side!=piece.side:
                captures.append((x,piece.position[1]))
                x=-1            
            else:
                x=-1 
    return  

def bishop(piece, moves, captures):
    x=piece.position[0]
    y=piece.position[1]
    while(x<8 and y<8):
        if board[x][y]==0:
            moves.append((x,y))
            x+=1
            y+=1
        elif board[x][y].side!=piece.side:
            captures.append((x,y))
            x=9
        else:
            x=9
    x=piece.position[0]
    y=piece.position[1]
    while(x>=0 and y>=0):
        if board[x][y]==0:
            moves.append((x,y))
            x-=1
            y-=1
        elif board[x][y].side!=piece.side:
            captures.append((x,y))
            x=-1
        else:
            x=-1
    while(x<8 and y>=0):
        if board[x][y]==0:
            moves.append((x,y))
            x+=1
            y-=1
        elif board[x][y].side!=piece.side:
            captures.append((x,y))
            x=9
        else:
            x=9

    x=piece.position[0]
    y=piece.position[1]
    while(x>=0 and y<8):
        if board[x][y]==0:
            moves.append((x,y))
            x-=1
            y+=1
        elif board[x][y].side!=piece.side:
            captures.append((x,y))
            x=-1
        else:
            x=-1
    return

def knight(piece, moves, captures):
    top=7-piece.position[0]
    bot=piece.position[0]
    right=7-piece.position[1]
    left=piece.position[1]
    if top>=2 and right >=1:
        if board[piece.position[0]+2][piece.position[1]+1] ==0:
            moves.append((piece.position[0]+2,piece.position[1]+1))
        elif board[piece.position[0]+2][piece.position[1]+1].side != piece.side:
            captures.append((piece.position[0]+2,piece.position[1]+1))
    if top>=2 and left >=1:
        if board[piece.position[0]+2][piece.position[1]-1] ==0:
            moves.append((piece.position[0]+2,piece.position[1]-1))
        elif board[piece.position[0]+2][piece.position[1]-1].side != piece.side:
            captures.append((piece.position[0]+2,piece.position[1]-1))
        
    if top>=1 and right >=2:
        if board[piece.position[0]+1][piece.position[1]+2] ==0:
            moves.append((piece.position[0]+1,piece.position[1]+2))
        elif board[piece.position[0]+1][piece.position[1]+2].side != piece.side:
            captures.append((piece.position[0]+1,piece.position[1]+2))
    if top>=1 and left >=2:
        if board[piece.position[0]+1][piece.position[1]-2] ==0:
            moves.append((piece.position[0]+1,piece.position[1]-2))
        elif board[piece.position[0]+1][piece.position[1]-2].side != piece.side:
            captures.append((piece.position[0]+1,piece.position[1]-2))
    
    if bot>=2 and right >=1:
        if board[piece.position[0]-2][piece.position[1]+1] ==0:
            moves.append((piece.position[0]-2,piece.position[1]+1))
        elif board[piece.position[0]-2][piece.position[1]+1].side != piece.side:
            captures.append((piece.position[0]-2,piece.position[1]+1))
    if bot>=2 and left >=1:
        if board[piece.position[0]-2][piece.position[1]-1] ==0:
            moves.append((piece.position[0]-2,piece.position[1]-1))
        elif board[piece.position[0]-2][piece.position[1]-1].side != piece.side:
            captures.append((piece.position[0]-2,piece.position[1]-1))
        
    if bot>=1 and right >=2:
        if board[piece.position[0]-1][piece.position[1]+2] ==0:
            moves.append((piece.position[0]-1,piece.position[1]+2))
        elif board[piece.position[0]-1][piece.position[1]+2].side != piece.side:
            captures.append((piece.position[0]-1,piece.position[1]+2))
    if bot>=1 and left >=2:
        if board[piece.position[0]-1][piece.position[1]-2] ==0:
            moves.append((piece.position[0]-1,piece.position[1]-2))
        elif board[piece.position[0]-1][piece.position[1]-2].side != piece.side:
            captures.append((piece.position[0]-1,piece.position[1]-2))
    return

print(validmoves(whitepieces))
print(validmoves(blackpieces))



