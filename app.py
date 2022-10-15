##pylint: disable=too-many-function-args


import pygame
from aiPlayer import chooseMove
from gamelogic import *
from pygame.locals import *
from piece import Piece
from move import Move



    
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
    blackpieces = (bR,bN,bB,bQ,bK,bB2,bN2,bR2, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8)
    pieces = [wR,wN,wB,wQ,wK,wB2,wN2,wR2, wP1,wP2,wP3,wP4,wP5,wP6,wP7,wP8, bR,bN,bB,bQ,bK,bB2,bN2,bR2, bP1,bP2,bP3,bP4,bP5,bP6,bP7,bP8]
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
    highlight = pygame.image.load("highlight.png")
    piec = pygame.image.load("piece.png")
    whiterook = pygame.image.load("whiterook.png")
    blackrook = pygame.image.load("blackrook.png")
    whitepawn = pygame.image.load("whitepawn.png")
    blackpawn = pygame.image.load("blackpawn.png")
    whiteQueen = pygame.image.load("whitequeen.png")
    blackQueen = pygame.image.load("blackqueen.png")
    whitebishop = pygame.image.load("whitebishop.png")
    blackbishop = pygame.image.load("blackbishop.png")
    whitehorse = pygame.image.load("whitehorse.png")
    blackhorse = pygame.image.load("blackhorse.png")
    whiteking = pygame.image.load("whiteking.png")
    blackking = pygame.image.load("blackking.png")
    # Use an extra offset to centre the  in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    piece_offset = (sq_sz-whiterook.get_width()) // 2


    moveSelectedFlag = False
    selectedMove = None
    ##käy palauttaa listan laillisista siirroista ja vastustajan nappuloista jotka voi ottaa. listat eivät sisällä päällekkäisyyksiä.
    ## palautus muotoa [([nappulan siirrot], [vihollisen nappulat jotka nappulalla voi ottaa]), (sama seuraavalle nappulalle )...]
 
    turn="w"
    while True:
            for row in range(n):           # Draw each row of the board.
                c_indx = row % 2           # Alternate starting color
                for col in range(n):       # Run through cols drawing squares
                    the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                    surface.fill(colors[c_indx], the_square)
                    # Now flip the color index for the next square
                    c_indx = (c_indx + 1) % 2
            # Look for an event from keyboard, mouse, etc.
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break;
            if ev.type == MOUSEBUTTONDOWN: 
                
                if ev.button == 1:
                    print(pygame.mouse.get_pos())
                    clickedSquare = board[7-int(pygame.mouse.get_pos()[1]/60)][int(pygame.mouse.get_pos()[0]/60)]
                    
                    if not moveSelectedFlag and clickedSquare!=0:
                        if clickedSquare.side == turn:
                            moveSelectedFlag = True
                            legal(clickedSquare, board)
                            print(clickedSquare)
                            selectedMove = clickedSquare
                    else:
                        print(pygame.mouse.get_pos())
                        clickedSquare2 = (7-int(pygame.mouse.get_pos()[1]/60),int(pygame.mouse.get_pos()[0]/60))
                        print(clickedSquare2)
                           
                        for move in selectedMove.moves:
                            if clickedSquare2[1]==move.square[1] and clickedSquare2[0]==move.square[0]:
                                if move.promotion:
                                    promotion(selectedMove, board)
                                    break
                                print("siirto")
                                print(selectedMove.position)
                                if(board[clickedSquare2[0]][clickedSquare2[1]]!=0):
                                    if selectedMove.char == "K" and move.capture.side == selectedMove.side:
                                        if selectedMove.position[1] < move.capture.position[1]:
                                            pos = selectedMove.position
                                            selectedMove.setPos((pos[0], 6))
                                            board[pos[0]][6] = selectedMove
                                            board[clickedSquare2[0]][clickedSquare2[1]].setPos((pos[0], 5))
                                            board[pos[0]][5] = move.capture
                                            board[clickedSquare2[0]][clickedSquare2[1]] = 0
                                            board[pos[0]][pos[1]] = 0
                                            break
                                        else:
                                            pos = selectedMove.position
                                            selectedMove.setPos((pos[0], 1))
                                            board[pos[0]][1] = selectedMove
                                            board[clickedSquare2[0]][clickedSquare2[1]].setPos((pos[0], 2))
                                            board[pos[0]][2] = move.capture
                                            board[clickedSquare2[0]][clickedSquare2[1]] = 0
                                            board[pos[0]][pos[1]] = 0
                                            break
                                        
                                    deleted = move.capture
                                    deleted.die()
                                print(selectedMove.position)
                                board[move.square[0]][move.square[1]]=selectedMove
                                board[selectedMove.position[0]][selectedMove.position[1]]=0
                                selectedMove.setPos((move.square[0],move.square[1]))
                                moveSelectedFlag=False
                                if turn == "w":
                                    turn="b"
                                else:
                                    turn="w"
                                break;
                        if moveSelectedFlag:
                            moveSelectedFlag=False
                        




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
                                if not board[i][j].alive:
                                    ##end game
                                     pass
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
                                if not board[i][j].alive:
                                    ##end game
                                     pass
                                surface.blit(blackking, ((j)*sq_sz+piece_offset,(420)-(i)*sq_sz+piece_offset))
                            if board[i][j].char == "B":
                                surface.blit(blackbishop, ((j)*sq_sz+piece_offset,420-(i)*sq_sz+piece_offset))
                    j+=1
                i+=1
                j=0
                
                if moveSelectedFlag:
                    for move in selectedMove.moves:
                        surface.blit(highlight, ((move.square[1])*sq_sz+piece_offset,420-(move.square[0])*sq_sz+piece_offset))
            
            if turn == "b":
                board = chooseMove(board, pieces)
                turn = "w"
                
            pygame.display.update()


    pygame.quit()


main()