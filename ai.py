from board import Tictactoe
import copy

class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self, pos:int):
        self.board.play(pos, "O")

    def minMax(self):
        if self.board.checkWinner():
            value = 0
            return value
        elif self.board.checkDraw():
            value = 1
            return value
        else:
            value = -1
            return value
        

    def resultState(self, board: Tictactoe, num: int):        
        acopy = copy.deepcopy(board)
        acopy.play(num, "O")
        return acopy

    




