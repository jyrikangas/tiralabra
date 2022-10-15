

class Piece(object):
    ##pelinappulalla on hahmo (ratsu, lähtetti, jne), puoli ('w' tai 'b'), ja koordinaatit pelilaudalla
    def __init__(self, char, side, position):
        self.char = char
        self.side = side
        self.position = position
        self.alive = True
        self.hasNotMoved = True
        self.moves = []
    
    def __str__(self) -> str:
        return self.char
    def __repr__(self) -> str:
        return self.char + " @ "+ str(self.position[0]) + str(self.position[1])
    
    def die(self):
        self.alive = False
        self.position = (-1, -1)
        return
    def setPos(self, pos):
        self.position = pos
        if self.hasNotMoved:
            self.hasNotMoved = False
        return