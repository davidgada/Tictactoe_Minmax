

class Tictactoe:
    def _init_(self):
        self.board = [[j for j in range (3)] for i in range (3)]
          

    def play(self, pos:int, piece:str):
        if pos < 3:
            self.board[0][pos] = "X"
        elif pos > 2 and pos < 6 :
            self.board[1][pos - 3] = "X"
        else:
            self.board[2][pos - 6] = "X"
    
    def printBoard(self):
        for num in self.board:
            print('I', num,)
            print('-'* 5)

    def checkWinner(self):
        if(self)

    
    


        





