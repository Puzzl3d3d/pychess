class Piece:
    def __init__(white):
        self.setWhite(white)
        self.setKilled(False)
    def isWhite():
        return self.white
    def setWhite(white):
        self.white = white
    def isKilled():
        return self.killed
    def setKilled(killed):
        self.killed = killed

# Create each piece as a child of the Piece category
class King(Piece):

    def __init__(self,white):
        super().__init__(white)
        self.setCastlingDone(False)

    def __init__():
        self.setCastlingDone(False)
    def isCastlingDone():
        return self.castlingDone
    def setCastlingDone(castlingDone):
        self.castlingDone = castlingDone
    def canMove(board, start, end):
        if (end.getPiece().isWhite() == this.isWhite()):
            return False
        
        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())

        if (x + y == 1):
            # Check here if king is being attacked
            return True
        
        return self.isValidCastling(board, start, end)
    def isValidCastling(board, start, end):
        if self.isCastlingDone():
            return False
        
        # Logic here for returning true or false
    def isCastlingMove(start, end):
        # Check if the starting and ending position are correct
        return False

class Knight(Piece):
    def __init__(self,white):
        super().__init__(white)
    def canMove(board, start, end):
        if (end.getPiece().isWhite() == this.isWhite()):
            return False

        x = abs(start.getX() - end.getX())
        y = abs(start.getY() - end.getY())

        return x * y == 2
# Create other pieces