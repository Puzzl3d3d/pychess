import chess
import chess.svg

import webbrowser, os

PRINT_BOARD = False
USE_SAN = True

move_format = "SAN" if USE_SAN else "UCI"

board = chess.Board()

player = "White"

def GetMove():
    print(player)
    move = input(f"Move to play ({move_format} format): ")

    try:
        if move.lower() == "takeback":
            return move.lower()
        if move.lower() == "resign":
            return move.lower()

        return {
            "UCI": str(board.parse_san(move)) if USE_SAN else move,
            "SAN": move if USE_SAN else str(board.parse_uci(move))
        }
    except:
        return ""
def ShowBoard():
    text = f"{player} to move"
    if board.is_game_over():
        text = "Game over"
    if board.is_checkmate():
        text = "Checkmate, " + ("White" if player == "Black" else "Black") + " won"
    if board.is_stalemate():
        text = "Stalemate! Draw..."
    if board.is_insufficient_material():
        text = "Insufficient material! Draw..."

    svg_data = chess.svg.board(board, size=700) + f"""<h1 style="font-size: 100px; font-family: 'Arial'; padding-left: 20px">{text}</h1>"""
    """ Loads the svg data to the webpage """
    file = open("display.html", "w")
    file.write(svg_data)
    file.close()

    webbrowser.open('file://' + os.path.realpath("display.html"), 0, autoraise=False)


ShowBoard()
if PRINT_BOARD: print(board)

while True:
    move = GetMove()
    if move == "": continue
    if move == "takeback":
        board.pop()
        print("Took back move")
        player = "Black" if player == "White" else "White"
        ShowBoard()
        if PRINT_BOARD: print(board)
        continue
    if move == "resign":
        print("Resigned!","White" if player == "Black" else "Black", "won!")
        break
    
    if chess.Move.from_uci(move["UCI"]) not in board.legal_moves:
        print("Illegal move!")
        continue
    if USE_SAN: 
        board.push_san(move["SAN"])
    else:
        board.push_uci(move["UCI"])
    move_ = move["SAN"] if USE_SAN else move["UCI"]
    print(f"Played move: {move_}")
    player = "Black" if player == "White" else "White"
    ShowBoard()
    if PRINT_BOARD: print(board)
    if board.is_checkmate():
        print("Checkmate!","White" if player == "Black" else "Black", "won!")
        break
    if board.is_stalemate():
        print("Stalemate! Draw...")
        break
    if board.is_insufficient_material():
        print("Insufficient material! Draw...")
        break
    if board.is_game_over():
        print("Game over")
        break