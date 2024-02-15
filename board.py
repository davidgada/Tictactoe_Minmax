

class Tictactoe:
    def __init__(self):
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
            print(' | '.join(num))
            print('-'* 10)

    def checkWinner(self): 
        checker = False       
        #Check for the rows
        for i in range (3):
            if checker == False:
                for j in range (2):
                    checker = self.comparePieces(self.board[i][j], self.board[i][j + 1])
                    if not checker:
                        break
            else:
                break

        if checker == False:
            #Check for the columns
            for j in range (3):
                if checker == False:
                    for i in range (2):
                        checker = self.comparePieces(self.board[i][j], self.board[i + 1][j])
                        if not checker:
                            break
                else:
                    break


        if checker == False:
            # Check for left to right diagonal
            checker = self.comparePieces(self.board[0][0], self.board[1][1]) and self.comparePieces(self.board[1][1], self.board[2][2])
        if checker == False:
            # Check for right to left diagonal
            checker = checker or (self.comparePieces(self.board[0][2], self.board[1][1]) and self.comparePieces(self.board[1][1], self.board[2][0]))   
        return checker
    
    #Check if all spaces are filled and the winning condition is not met 
    def checkDraw(self):  
        check = True                     
        for i in range (3):
            if check == True:   
                for j in range (3):
                    if self.board[i][j] == "A":
                        check = False
                        break
                        print("Shouldn't run here")
                    else:
                        check = True
                    if j == 2:
                        break
            else:
                break
        return check
    
    def gameOver(self):
        if self.checkDraw() == True or self.checkWinner() == True:
            return True
        else:
            return False               


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
        
    def checkTurn(self):
        aiturn = 0
        pturn = 0        
        for i in range (3):             
            for j in range (3):
                if self.board[i][j] == "O":
                    aiturn =+ 1
                elif self.board =="X":
                    pturn += 1

        if pturn > aiturn:
            return "Min"
        elif aiturn > pturn:
            return "Max"
    
        
   

        

        

    
    


        





