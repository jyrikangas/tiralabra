##pylint: disable=too-many-function-args


import pygame
from piece import Piece
from move import Move
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

## aloita loop
## luo kuva, kutsu metodeja, ota input, tee siirto, päivitä kuva, repeat.
## lopetus?

pygame.init()
colors = [(255,0,0), (0,0,0)]  
main_surface = pygame.display.set_mode((480,240))
n = len(board)         # This is an NxN chess board.
surface_sz = 480           # Proposed physical surface size.
sq_sz = surface_sz // n    # sq_sz is length of a square.
surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
# Create the surface of (width, height), and its window.
surface = pygame.display.set_mode((surface_sz, surface_sz))
piec = pygame.image.load("piece.png")
# Use an extra offset to centre the  in its square.
# If the square is too small, offset becomes negative,
#   but it will still be centered :-)
piece_offset = (sq_sz-piec.get_width()) // 2

while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        ## piirrä nappulat
        i=0
        j=0
        while(i<8):
            while(j<8):
                ## lisää muunlaiset nappulat
                if board[i][j] != 0:
                    surface.blit(piec, ((j)*sq_sz+piece_offset,(i)*sq_sz+piece_offset))
                j+=1
            i+=1
            j=0
        pygame.display.flip()


pygame.quit()
##käy palauttaa listan laillisista siirroista ja vastustajan nappuloista jotka voi ottaa. listat eivät sisällä päällekkäisyyksiä.
## palautus muotoa [([nappulan siirrot], [vihollisen nappulat jotka nappulalla voi ottaa]), (sama seuraavalle nappulalle )...]
def validmoves(pieces):
    moves = []
    for piece in pieces:
        legal(piece)
        print(piece.char + "@" +str(piece.position))
        print(piece.moves)
    
    return 
    
##käy läpi kohdat joihin nappula voi siirtyä ja palauttaa listat ruuduista joihin nappulan voi siirtää ja joihin se voi siirtyä mutta joissa on vastustajan nappula.
def legal(piece):
    
    if piece.char == "P":
        if piece.side == "w":
            ## jos sotilas on aloitusruudussa, se voi siirtyä kahteen edessä olevaan ruutuun, jos ne ovat tyhjiä
            if piece.position[0]==1:
                if board[2][piece.position[1]]==0:
                    piece.moves.append(Move((2,piece.position[1]),board[2][piece.position[1]]))
                if board[3][piece.position[1]]==0:
                    piece.moves.append(Move((3,piece.position[1]),board[3][piece.position[1]]))
            
            if piece.position[0]<7:
                ## jos edessä oleva ruutu on tyhjä, sotilas voi liikkua eteenpäin
                if board[piece.position[0]+1][piece.position[1]]==0:
                    piece.moves.append(Move((piece.position[0]+1,piece.position[1]),board[piece.position[0]+1][piece.position[1]]))
                ## nämä rivit tarkastavat onko nappula laudan reunalla, ja jos laudalla olevalla etuviistossa sijaitsevalla ruudulla on vastapuolen nappula, se voidaan lisätä siirtolistaan.
                if piece.position[1]<7:
                    if board[piece.position[0]+1][piece.position[1]+1]!=0:
                        if board[piece.position[0]+1][piece.position[1]+1].side=="b":
                            piece.moves.append(Move((piece.position[0]+1,piece.position[1]+1),board[piece.position[0]+1][piece.position[1]+1]))
                if piece.position[1]>0:
                    if board[piece.position[0]+1][piece.position[1]-1]!=0:
                        if board[piece.position[0]+1][piece.position[1]-1].side=="b":
                            piece.moves.append(Move((piece.position[0]+1,piece.position[1]-1),board[piece.position[0]+1][piece.position[1]-1]))
            
        else:
            ## jos sotilas (musta) on aloitusruudussa, se voi siirtyä kahteen edessä olevaan ruutuun, jos ne ovat tyhjiä
            if piece.position[0]==6:
                if board[5][piece.position[1]]==0:
                    piece.moves.append(Move((5,piece.position[1]),board[5][piece.position[1]]))
                if board[4][piece.position[1]]==0:
                    piece.moves.append(Move((4,piece.position[1]),board[4][piece.position[1]]))
            ## jos edessä oleva ruutu on pelilaudalla ja tyhjä, sotilas voi liikkua eteenpäin
            if piece.position[0]>0:
                if board[piece.position[0]-1][piece.position[1]]==0:
                    piece.moves.append(Move((piece.position[0]-1,piece.position[1]),board[piece.position[0]-1][piece.position[1]]))
                ## nämä rivit tarkastavat onko nappula laudan reunalla, ja jos laudalla olevalla etuviistossa sijaitsevalla ruudulla on vastapuolen nappula, se voidaan lisätä siirtolistaan.
                if piece.position[1]<7:
                    if board[piece.position[0]-1][piece.position[1]+1]!=0:
                        if board[piece.position[0]-1][piece.position[1]+1].side=="w":
                            piece.moves.append(Move((piece.position[0]-1,piece.position[1]+1),board[piece.position[0]-1][piece.position[1]+1]))
                if piece.position[1]>0:
                    if board[piece.position[0]-1][piece.position[1]-1]!=0:
                        if board[piece.position[0]-1][piece.position[1]-1].side=="w":
                            piece.moves.append(Move((piece.position[0]-1,piece.position[1]-1),board[piece.position[0]-1][piece.position[1]-1]))

    if piece.char == "R":
        rook(piece)
    if piece.char == "N":
        knight(piece)
    if piece.char == "B":
        bishop(piece)
    if piece.char == "Q":
        rook(piece)
        bishop(piece)
    if piece.char == "K":
        x =max(piece.position[0]-1,0)
        y =max(piece.position[1]-1,0)
        xend = min(piece.position[0]+1,7)
        yend = min(piece.position[1]+1,7)
        while(x<=xend):
            while(y<=yend):
                if board[x][y]==0:
                    piece.moves.append(Move((x,y),board[x][y]))
                    y+=1
                elif board[x][y].side!=piece.side:
                    piece.moves.append(Move((x,y),board[x][y]))
                    y+=1
                else:
                    y+=1
            x+=1
    return 
    

def rook(piece):
    x=piece.position[0]
    y=piece.position[1]
    while y<8:
        if board[piece.position[0]][y]==0:
            piece.moves.append(Move((piece.position[0],y), board[piece.position[0]][y]))
            y+=1
        elif board[piece.position[0]][y].side!=piece.side:
            piece.moves.append(Move((piece.position[0],y), board[piece.position[0]][y]))
            y=9  
        else:
            y=9  
    while x<8:
        if board[x][piece.position[1]]==0:
            piece.moves.append(Move((x,piece.position[1]),board[x][piece.position[1]]))
            x+=1
        elif board[x][piece.position[1]].side!=piece.side:
            piece.moves.append(Move((x,piece.position[1]),board[x][piece.position[1]]))
            x=8            
        else:
            x=8 
    
    
    x=piece.position[0]
    y=piece.position[1]
    while y>=0:
        if board[piece.position[0]][y]==0:
            piece.moves.append(Move((piece.position[0],y), board[piece.position[0]][y]))
            y-=1
        elif board[piece.position[0]][y].side!=piece.side:
            piece.moves.appendMove((piece.position[0],y), board[piece.position[0]][y])
            y=-1  
        else:
            y=-1  
        while x>=0:
            if board[x][piece.position[1]]==0:
                piece.moves.append(Move((x,piece.position[1]),board[x][piece.position[1]]))
                x-=1
            elif board[x][piece.position[1]].side!=piece.side:
                piece.moves.append(Move((x,piece.position[1]),board[x][piece.position[1]]))
                x=-1            
            else:
                x=-1 
    return  

def bishop(piece,):
    x=piece.position[0]
    y=piece.position[1]
    while(x<8 and y<8):
        if board[x][y]==0:
            piece.moves.append(Move((x,y),board[x][y]))
            x+=1
            y+=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((x,y),board[x][y]))
            x=9
        else:
            x=9
    x=piece.position[0]
    y=piece.position[1]
    while(x>=0 and y>=0):
        if board[x][y]==0:
            piece.moves.append(Move((x,y),board[x][y]))
            x-=1
            y-=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((x,y),board[x][y]))
            x=-1
        else:
            x=-1
    while(x<8 and y>=0):
        if board[x][y]==0:
            piece.moves.append(Move((x,y),board[x][y]))
            x+=1
            y-=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((x,y),board[x][y]))
            x=9
        else:
            x=9

    x=piece.position[0]
    y=piece.position[1]
    while(x>=0 and y<8):
        if board[x][y]==0:
            piece.moves.append(Move((x,y),board[x][y]))
            x-=1
            y+=1
        elif board[x][y].side!=piece.side:
            piece.moves.append(Move((x,y),board[x][y]))
            x=-1
        else:
            x=-1
    return

def knight(piece,):
    top=7-piece.position[0]
    bot=piece.position[0]
    right=7-piece.position[1]
    left=piece.position[1]
    if top>=2 and right >=1:
        if board[piece.position[0]+2][piece.position[1]+1] ==0:
            piece.moves.append(Move((piece.position[0]+2,piece.position[1]+1), board[piece.position[0]+2][piece.position[1]+1]))
        elif board[piece.position[0]+2][piece.position[1]+1].side != piece.side:
            piece.moves.append(Move((piece.position[0]+2,piece.position[1]+1), board[piece.position[0]+2][piece.position[1]+1]))
    if top>=2 and left >=1:
        if board[piece.position[0]+2][piece.position[1]-1] ==0:
            piece.moves.append(Move((piece.position[0]+2,piece.position[1]-1), board[piece.position[0]+2][piece.position[1]-1]))
        elif board[piece.position[0]+2][piece.position[1]-1].side != piece.side:
            piece.moves.append(Move((piece.position[0]+2,piece.position[1]-1), board[piece.position[0]+2][piece.position[1]-1]))
        
    if top>=1 and right >=2:
        if board[piece.position[0]+1][piece.position[1]+2] ==0:
            piece.moves.append(Move((piece.position[0]+1,piece.position[1]+2), board[piece.position[0]+1][piece.position[1]+2]))
        elif board[piece.position[0]+1][piece.position[1]+2].side != piece.side:
            piece.moves.append(Move((piece.position[0]+1,piece.position[1]+2), board[piece.position[0]+1][piece.position[1]+2]))
    if top>=1 and left >=2:
        if board[piece.position[0]+1][piece.position[1]-2] ==0:
            piece.moves.append(Move((piece.position[0]+1,piece.position[1]-2), board[piece.position[0]+1][piece.position[1]-2]))
        elif board[piece.position[0]+1][piece.position[1]-2].side != piece.side:
            piece.moves.append(Move((piece.position[0]+1,piece.position[1]-2), board[piece.position[0]+1][piece.position[1]-2]))
    
    if bot>=2 and right >=1:
        if board[piece.position[0]-2][piece.position[1]+1] ==0:
            piece.moves.append(Move((piece.position[0]-2,piece.position[1]+1), board[piece.position[0]-2][piece.position[1]+1]))
        elif board[piece.position[0]-2][piece.position[1]+1].side != piece.side:
            piece.moves.append(Move((piece.position[0]-2,piece.position[1]+1), board[piece.position[0]-2][piece.position[1]+1]))
    if bot>=2 and left >=1:
        if board[piece.position[0]-2][piece.position[1]-1] ==0:
            piece.moves.append(Move((piece.position[0]-2,piece.position[1]-1), board[piece.position[0]-2][piece.position[1]-1]))
        elif board[piece.position[0]-2][piece.position[1]-1].side != piece.side:
            piece.moves.append(Move((piece.position[0]-2,piece.position[1]-1), board[piece.position[0]-2][piece.position[1]-1]))
        
    if bot>=1 and right >=2:
        if board[piece.position[0]-1][piece.position[1]+2] ==0:
            piece.moves.append(Move((piece.position[0]-1,piece.position[1]+2), board[piece.position[0]-1][piece.position[1]+2]))
        elif board[piece.position[0]-1][piece.position[1]+2].side != piece.side:
            piece.moves.append(Move((piece.position[0]-1,piece.position[1]+2), board[piece.position[0]-1][piece.position[1]+2]))
    if bot>=1 and left >=2:
        if board[piece.position[0]-1][piece.position[1]-2] ==0:
            piece.moves.append(Move((piece.position[0]-1,piece.position[1]-2), board[piece.position[0]-1][piece.position[1]-2]))
        elif board[piece.position[0]-1][piece.position[1]-2].side != piece.side:
            piece.moves.append(Move((piece.position[0]-1,piece.position[1]-2), board[piece.position[0]-1][piece.position[1]-2]))
    return

print(validmoves(whitepieces))
print(validmoves(blackpieces))



