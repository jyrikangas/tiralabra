

class Move(object):
    def __init__(self, origin, square, squarecontent):
        self.origin = origin
        self.square = square
        self.promotion = False
        if squarecontent != 0:
            self.capture = squarecontent
            
            
        else:
            self.capture = 0
    def set_promotion(self, promotion):
        self.promotion = promotion
        return
        
    @classmethod
    def makePromotion(cls, origin, square, squarecontent, promotion):
        move = cls(origin, square, squarecontent)
        move.set_promotion(promotion)
        return move
    
    def __repr__(self) -> str:
        return str(self.square) + "-->" + str(self.capture)
    
    def setValue(self, value):
        self.value = value