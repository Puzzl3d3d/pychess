class Player:
    def isWhiteSide():
        return self.white
    def isHumanPlayer():
        return self.human

class HumanPlayer(Player):
    def __init__(white):
        self.white = white
        self.human = True
class ComputerPlayer(Player):
    def __init__(white):
        self.white = white
        self.human = False