from board import Tictactoe
import copy
import math

class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self):
        bvalue= -math.inf
        baction = -1
        for a in self.board.actionSpace():
            # self.resultState(self.board, a)
            value = self.MiniMax(self.board)
            # (self.resultState(self.board, a)).undoplay(a)
            if(value > bvalue):
                bvalue = value
                baction = a
            self.board.play(baction, "O")
            

    def MiniMax(self, board: Tictactoe):
        if self.board.checkWinner():           
            return 1 
        elif self.board.checkDraw():
            return 0
        else:
            return -1
        values = []
        if(self.board.checkTurn()== "Max"):
            for a in self.board.actionSpace():
                values.append(Minimax(self.resultState(self.board, a))) 
                    
            return max(values)
        
        if(self.board.checkTurn()== "Min"):
            for a in self.board.actionSpace():
                values.append(Minimax(self.resultState(self.board, a))) 
                    
            return min(values)


            
        

    def resultState(self, board: Tictactoe, num: int):        
        acopy = copy.deepcopy(board)
        acopy.play(num, "O")
        return acopy

    




