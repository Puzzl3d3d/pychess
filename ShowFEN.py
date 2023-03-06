import chess
import chess.svg

import webbrowser, os

board = chess.Board(input("Input FEN: "))

def ShowBoard(board):
    svg_data = chess.svg.board(board, size=700)
    """ Loads the svg data to the webpage """
    file = open("display.html", "w")
    file.write(svg_data)
    file.close()

    webbrowser.open('file://' + os.path.realpath("display.html"), 0, autoraise=False)

ShowBoard(board)