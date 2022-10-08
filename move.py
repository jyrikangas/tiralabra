

class Move(object):
    def __init__(self, square, squarecontent):
        self.square = square
        if squarecontent != 0:
            self.capture=squarecontent
        else:
            self.capture=0
        
    def __repr__(self) -> str:
        return str(self.square) + "-->" + str(self.capture)