GameStatus = {
    "ACTIVE": 1,
    "BLACK_WIN": 2,
    "WHITE_WIN": 3,
    "FORFEIT": 4,
    "STALEMATE": 5,
    "RESIGNATION": 6
}

class Move:
    def __init__(player, start, end):
        self.player = player
        self.start = start
        self.end = end
        self.pieceMoved = start.getPiece()
    def isCastlingMove():
        return self.castlingMove
    def setCastlingMove(castlingMove):
        self.castlingMove = castlingMove