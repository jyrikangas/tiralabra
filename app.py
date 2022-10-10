##pylint: disable=too-many-function-args


import pygame
from pygame.locals import *
from piece import Piece
from move import Move


def validmoves(pieces, board):
    moves = []
    for piece in pieces:
        legal(piece, board)
       ##print(piece.char + "@" +str(piece.position))
       ##print(piece.moves)
    
    return 
    
##käy läpi kohdat joihin nappula voi siirtyä ja palauttaa listat ruuduista joihin nappulan voi siirtää ja joihin se voi siirtyä mutta joissa on vastustajan nappula.
def legal(piece, board):
    
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
        rook(piece, board)
    if piece.char == "N":
        knight(piece, board)
    if piece.char == "B":
        bishop(piece, board)
    if piece.char == "Q":
        rook(piece, board)
        bishop(piece, board)
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
    

def rook(piece, board):
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

def bishop(piece, board):
    x=piece.position[0]+1
    y=piece.position[1]+1
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
    x=piece.position[0]-1
    y=piece.position[1]-1
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

    x=piece.position[0]+1
    y=piece.position[1]-1
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

    x=piece.position[0]-1
    y=piece.position[1]+1
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

def knight(piece, board):
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
def main():
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
    blackpieces = (bR,bN,bB,bQ,bK,bB2,bN2,bR, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8)
    ##pelilauta
    board = [[wR,wN,wB,wQ,wK,wB2,wN2,wR2], [wP1,wP2,wP3,wP4,wP5,wP6,wP7,wP8], 
    [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], 
    [bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8], [bR,bN,bB,bQ,bK,bB2,bN2,bR2]]
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
    highlight =pygame.image.load("highlight.png")
    piec = pygame.image.load("piece.png")
    whiterook =pygame.image.load("whiterook.png")
    blackrook =pygame.image.load("blackrook.png")
    whitepawn =pygame.image.load("whitepawn.png")
    blackpawn =pygame.image.load("blackpawn.png")
    whiteQueen =pygame.image.load("whitequeen.png")
    blackQueen =pygame.image.load("blackqueen.png")
    whitebishop =pygame.image.load("whitebishop.png")
    blackbishop =pygame.image.load("blackbishop.png")
    whitehorse =pygame.image.load("whitehorse.png")
    blackhorse =pygame.image.load("blackhorse.png")
    whiteking =pygame.image.load("whiteking.png")
    blackking =pygame.image.load("blackking.png")
    # Use an extra offset to centre the  in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    piece_offset = (sq_sz-whiterook.get_width()) // 2


    ##käy palauttaa listan laillisista siirroista ja vastustajan nappuloista jotka voi ottaa. listat eivät sisällä päällekkäisyyksiä.
    ## palautus muotoa [([nappulan siirrot], [vihollisen nappulat jotka nappulalla voi ottaa]), (sama seuraavalle nappulalle )...]
    while True:
            for row in range(n):           # Draw each row of the board.
                c_indx = row % 2           # Alternate starting color
                for col in range(n):       # Run through cols drawing squares
                    the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                    surface.fill(colors[c_indx], the_square)
                    # Now flip the color index for the next square
                    c_indx = (c_indx + 1) % 2
            # Look for an event from keyboard, mouse, etc.
            i=0
            j=0
            while(i<8):
                while(j<8):
                    ## lisää muunlaiset nappulat
                    if board[i][j] != 0:
                        if board[i][j].side=="w":
                            if board[i][j].char == "P":
                                surface.blit(whitepawn, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "R":
                                surface.blit(whiterook, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "N":
                                surface.blit(whitehorse, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "Q":
                                surface.blit(whiteQueen, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "K":
                                surface.blit(whiteking, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "B":
                                surface.blit(whitebishop, ((j)*sq_sz+piece_offset,420-piece_offset-(i)*sq_sz+piece_offset))
                        if board[i][j].side=="b":
                            if board[i][j].char == "P":
                                surface.blit(blackpawn, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "R":
                                surface.blit(blackrook, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "N":
                                surface.blit(blackhorse, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "Q":
                                surface.blit(blackQueen, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "K":
                                surface.blit(blackking, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "B":
                                surface.blit(blackbishop, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                    j+=1
                i+=1
                j=0
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break;
            if ev.type == MOUSEBUTTONDOWN: 
                validmoves(whitepieces, board)
                validmoves(blackpieces, board)
                if ev.button == 1:
                    print(pygame.mouse.get_pos())
                    clickedSquare = board[7-int(pygame.mouse.get_pos()[1]/60)][int(pygame.mouse.get_pos()[0]/60)]
                    if clickedSquare != 0:
                        while(True):
                            ev1 = pygame.event.poll()
                            if ev1.type == pygame.QUIT:
                                break;
                            if ev1.type == MOUSEBUTTONDOWN:
                                if ev1.button == 1:
                                    print(pygame.mouse.get_pos())
                                    clickedSquare2 = (7-int(pygame.mouse.get_pos()[1]/60),int(pygame.mouse.get_pos()[0]/60))
                                    print(clickedSquare2)
                                    
                                    for move in clickedSquare.moves:
                                        if clickedSquare2[1]==move.square[1] and clickedSquare2[0]==move.square[0]:
                                            print("siirto")
                                            clickedSquare.setPos((move.square[0],move.square[1]))
                                            board[move.square[0]][move.square[1]]=(board[clickedSquare.position[0]][clickedSquare.position[1]])
                                            
                                            board[clickedSquare.position[0]][clickedSquare.position[1]]=0
                                            break;
                                    if clickedSquare2 == 0:

                                        break;

                            for move in clickedSquare.moves:

                                print(move)
                                surface.blit(highlight, ((move.square[1])*sq_sz+piece_offset,420-(move.square[0])*sq_sz+piece_offset))
                                ## ruutu on pos/60 pyöristettynä alaspäin

                            pygame.display.update()


            ## piirrä nappulat
            i=0
            j=0
            while(i<8):
                while(j<8):
                    ## lisää muunlaiset nappulat
                    if board[i][j] != 0:
                        if board[i][j].side=="w":
                            if board[i][j].char == "P":
                                surface.blit(whitepawn, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "R":
                                surface.blit(whiterook, ((j)*sq_sz+piece_offset,420-((i)*sq_sz+piece_offset)))
                            if board[i][j].char == "N":
                                surface.blit(whitehorse, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "Q":
                                surface.blit(whiteQueen, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "K":
                                surface.blit(whiteking, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "B":
                                surface.blit(whitebishop, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                        if board[i][j].side=="b":
                            if board[i][j].char == "P":
                                surface.blit(blackpawn, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "R":
                                surface.blit(blackrook, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "N":
                                surface.blit(blackhorse, ((j)*sq_sz+piece_offset,420-(i)*sq_sz-piece_offset))
                            if board[i][j].char == "Q":
                                surface.blit(blackQueen, ((j)*sq_sz+piece_offset,420-(i)*sq_sz-piece_offset))
                            if board[i][j].char == "K":
                                surface.blit(blackking, ((j)*sq_sz+piece_offset,(420)-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "B":
                                surface.blit(blackbishop, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                    j+=1
                i+=1
                j=0




                        ## ruutu on pos/60 pyöristettynä alaspäin.
            pygame.display.update()


    pygame.quit()

main()
