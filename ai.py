from board import Tictactoe
import copy
import math

class Ai:
    def __init__(self, board:Tictactoe):
        self.board = board

    def play(self):
        print("My move","\n")  
        bvalue= -math.inf
        baction = None
        for a in self.board.actionSpace():
            # self.resultState(self.board, a)
            value = self.MiniMax(self.board)
            # (self.resultState(self.board, a)).undoplay(a)
            if(value > bvalue):
                bvalue = value
                baction = a
            self.board.play(baction, "O")
            

    def MiniMax(self, board: Tictactoe):
        if board.checkWinner():
        # If the maximizing player wins, return a positive value
            if board.checkWhoWon() == "O":
                return 1
        # If the minimizing player wins, return a negative value
            elif board.checkWhoWon() == "X":
                return -1
    # If the game ends in a draw, return 0
        elif board.checkDraw():
            return 0
        # else:
        # # If the game is not over, return a special value to indicate the non-terminal state
        #     return None


        
        values = []
        for a in board.actionSpace():
            values.append(self.MiniMax(self.resultState(board, a))) 


        if(board.checkTurn()== "Max"):
            return max(values)
            print("Running")
        
        else:   
                          
            return min(values)


            
        

    def resultState(self, board: Tictactoe, num: int):        
        acopy = copy.deepcopy(board)
        acopy.play(num, "O")
        return acopy

    




