from board import Tictactoe


class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self, pos:int):
        self.board.play(pos, "O")

    def minMax()
