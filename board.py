

class Tictactoe:
    def _init_(self):
        self.board = [["A" for  j in range (3)] for i in range (3)]
          

    def play(self, pos:int, piece:str):
        if pos < 3:
            self.board[0][pos] = piece
        elif pos > 2 and pos < 6 :
            self.board[1][pos - 3] = piece
        else:
            self.board[2][pos - 6] = piece
    
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
        it1 = 0
        jt1 = 0
        while i1 < 3 and j1 < 3:
            checker = self.board.comparePieces([i1][j1], [it1][jt1])
            it1 += 1
            jt1 += 1




        i2 = 0
        j2 = 2
        it2 = 0
        jt2 = 2
        while i2 < 3 and j2 < 3:
            checker = self.board.comparePieces([i2][j2], [it2][jt2])
            it2 += 1
            jt2 -= 1
   

 


        
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
        

        

    
    


        





