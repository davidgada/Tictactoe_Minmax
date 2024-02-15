from board import Tictactoe


class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self, pos:int):
        self.board.play(pos, "O")

    def minMax(self):
        if self.board.checkDraw():
            value = 0
            return value
        elif self.board.checkWinner():
            value = 1
            return value
        else:
            value = -1
            return value
        


