from Spot import Spot
from Piece import *

class Board():
    def __init__():
        self.resetBoard()
    def getBox(x, y):
        assert(not (x < 0 or x > 7 or y < 0 or y > 7), "Index out of bound")
  
        return boxes[x][y]
    def resetBoard():
        # initialize white pieces
        self.boxes = []
        self.boxes[0][0] = Spot(0, 0, Rook(true))
        self.boxes[0][1] = Spot(0, 1, Knight(true))
        self.boxes[0][2] = Spot(0, 2, Bishop(true))
        self.boxes[0][3] = Spot(0, 3, Queen(true))
        self.boxes[0][4] = Spot(0, 4, King(true))
        self.boxes[0][5] = Spot(0, 5, Bishop(true))
        self.boxes[0][6] = Spot(0, 6, Knight(true))
        self.boxes[0][7] = Spot(0, 7, Rook(true))
        # Pawns
        for i in range(8):
            self.boxes[1][i] = Spot(1, i, Pawn(true))
  
        # initialize black pieces
        self.boxes[7][0] = Spot(0, 0, Rook(true))
        self.boxes[7][1] = Spot(0, 1, Knight(true))
        self.boxes[7][2] = Spot(0, 2, Bishop(true))
        self.boxes[7][3] = Spot(0, 3, Queen(true))
        self.boxes[7][4] = Spot(0, 4, King(true))
        self.boxes[7][5] = Spot(0, 5, Bishop(true))
        self.boxes[7][6] = Spot(0, 6, Knight(true))
        self.boxes[7][7] = Spot(0, 7, Rook(true))
        # Pawns
        for i in range(8):
            self.boxes[6][i] = Spot(1, i, Pawn(false))
  
        # initialize remaining boxes without any piece
        for i in range(2, 5, 1):
            for j in range(0, 7, 1):
                self.boxes[i][j] = Spot(i, j, None);
    