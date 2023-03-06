from Board import Board
from Move import *

class Game:
    def __init__(p1, p2):
        self.players = [p1, p2]
        self.board = Board()
        self.board.resetBoard()
        self.movesPlayed = []

        if p1.isWhiteSide():
            self.currentTurn = p1
        else:
            self.currentTurn = p2
    def isEnd():
        return self.getStatus != GameStatus["ACTIVE"]
    def getStatus():
        return self.status
    def setStatus(status):
        self.status = status
    def playerMove(player, startX, startY, endX, endY):
        startBox = self.board.getBox(startX, startY)
        endBox = self.board.getBox(endX, endY)

        move = Move(player, startBox, endBox)
        return self.makeMove(move, player)
    def makeMove(move, player):
        sourcePiece = move.getStart().getPiece()
        if not sourcePiece:
            return False

        if player != self.currentTurn:
            return False

        if sourcePiece.isWhite() != player.isWhiteSide():
            return False

        if not sourcePiece.canMove(board, move.getStart(), move.getEnd()):
            return False

        destPiece = move.getEnd().getPiece()
        if not destPiece:
            destPiece.setKilled(True)
            move.setPieceKilled(destPiece)
        
        if sourcePiece and type(sourcePiece).__name__ == "King" and sourcePiece.isCastlingMove(): # very hacky fix lol
            move.setCastlingMove(True)
        
        self.movesPlayed.append(move)

        move.getEnd().setPiece(move.getStart().getPiece())
        move.getStart().setPiece(None)

        if destPiece and type(destPiece).__name__ == "King":
            if player.isWhiteSide():
                self.setStatus(GameStatus["WHITE_WIN"])
            else:
                self.setStatus(GameStatus["BLACK_WIN"])
        
        if self.currentTurn == players[0]:
            self.currentTurn = players[1]
        else:
            self.currentTurn = players[0]
        
        return True
            