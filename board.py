

class Tictactoe:
    def _init_(self):
        self.board = [["A" for  j in range (3)] for i in range (3)]
          

    def play(self, pos:int, piece:str):
        if pos < 3:
            self.board[0][pos] = "X"
        elif pos > 2 and pos < 6 :
            self.board[1][pos - 3] = "X"
        else:
            self.board[2][pos - 6] = "X"
    
    def printBoard(self):
        for num in self.board:
            print('I'.join(num))
            print('-'* 5)

    def checkWinner(self):
        checker = False
        for i in range (3):
            for j in range (3):
                checker = self.board.comparePieces([i][j], [i][j + 1])
                if j == 2:
                    break
        

        for i in range (3):
            for j in range (3):
                checker = self.board.comparePieces([i][j], [i + 1][j])
                if i == 2:
                    break


        i1 = 0
        j1 = 0
        while i1 < 3 and j1 < 3:
            checker = self.board.comparePieces([i1][j1], [i1 + 1][j1 + 1])
            i1 += 1
            j1 += 1

        i2 = 0
        j2 = 2
        while i2 < 3 and j2 < 3:
            checker = self.board.comparePieces([i2][j2], [i2 + 1][j2 - 1])
            i2+= 1
            j2 += 1





        for i in range (3):
            for j in range (3):
                checker = self.board.comparePieces([i][j], [i + 1],[j + 1])
                if i == 2 or j == 2:
                    break


        for i in range (3):
            for j in range (3):
                checker = self.board.comparePieces([i][j], [i + 1],[j + 1])
                if i == 2 or j == 2:
                    break
        
        


        
        return checker



    def comparePieces(self, a:str, b:str):
        if a == "A":
            return False
        elif b == "A":
            return False
        elif a == "X" and b == "X":
            return True
        elif a == "O" and b == "O":
            return True 
        else:
            return False
        

        

    
    


        





