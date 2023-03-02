import chess
import chess.svg

board = chess.Board()

print(chess.svg.board(board))

playernum = 1

while True:
    move = input("Input move: ")
    if move == "takeback":
        board.pop()
        print("Took back move")
        print(chess.svg.board(board))#print(board)
        playernum = 1 if playernum==0 else 0
        continue
    if move == "resign":
        print("Resigned!","White" if playernum==0 else "Black", "won!")
        break
    if chess.Move.from_uci(move) not in board.legal_moves:
        print("Illegal move!")
        continue
    board.push_uci(move)
    print(f"Played {move}")
    print(chess.svg.board(board))#print(board)
    playernum = 1 if playernum==0 else 0
    if board.is_checkmate():
        print("Checkmate!","White" if playernum==0 else "Black", "won!")
        break