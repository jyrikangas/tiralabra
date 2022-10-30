
##
# pelinappulalla on hahmo (ratsu, lähtetti, jne), puoli ('w' tai 'b'),
#  ja koordinaatit pelilaudalla. LIsäksi lista siirroista joita nappula voi tehdä,
#  ja  bool arvot alive ja hasNotMoved,
#  jotka kertovat onko nappula pelissä ja onko se liikkunut (linnoitusta varten) 
##
class Piece(object):
    
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
        return self.side + self.char + " @ "+ str(self.position[0]) + str(self.position[1])
    
    ##nappula poistuu pelistä
    def die(self):
        self.alive = False
        self.position = (-1, -1)
        return

    ##käytetään nappulan sijainnin päivittämiseen
    def setPos(self, pos):
        self.position = pos
        if self.hasNotMoved:
            self.hasNotMoved = False
        return
    