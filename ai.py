from board import Tictactoe
import copy
import math

class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self, pos:int):
        bvalue= -math.inf
        baction = -1
        for a in self.board.actionSpace():
            self.resultState(self.board, a)
            value = self.MinMax()
            (self.resultState(self.board, a)).undoplay(a)
            if(value > bvalue):
                bvalue = value
                baction = a
            self.board.play(baction, "O")
            

    def MiniMax(self):
        if self.board.checkWinner():           
            return 1, 
        elif self.board.checkDraw():
            return 0
        else:
            return -1
        values = []
        for a in self.board.actionSpace():
                self.board.play(a, "O")
                values.append(Minimax()) = max(value, self.MiniMax(resultState(self.board, a)))
                self.board.undoplay(a)


            
        

    def resultState(self, board: Tictactoe, num: int):        
        acopy = copy.deepcopy(board)
        acopy.play(num, "O")
        return acopy

    




