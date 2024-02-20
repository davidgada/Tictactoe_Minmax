import copy

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
    
    #Check if all spaces are filled and  
    
    def checkDraw(self):  
        check = True                     
        for i in range (3):
            if check == True:   
                for j in range (3):
                    if self.board[i][j] == "A":
                         check = False
                         break
                    else:
                        check = True
                    if j == 2:
                        break
            else:
                break
        return check

    def isGameOver(self):
        if self.checkWinner() == True or self.checkDraw() == True:
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
        #Ai plays O, max
        #Player plays x, min
        #Ai always plays first
        aicount = 0
        pcount = 0        
        for i in range (3):             
            for j in range (3):
                if self.board[i][j] == "O":
                    aicount =+ 1                    
                elif self.board[i][j] =="X":
                    pcount += 1                
        if pcount > aicount:
            return "Max"
        elif aicount >= pcount:
            return "Min"
        

    def actionSpace(self):
            actionList = []
            for i in range (3):             
                for j in range (3):
                    if self.board[i][j] == "A" and i == 0:
                        actionList.append(j)
                    elif self.board[i][j] == "A" and i == 1:
                        if j == 0:
                            actionList.append(3)
                        elif j == 1:
                            actionList.append(4)
                        elif j == 2:
                            actionList.append(5)
                    elif self.board[i][j] == "A" and i == 2:
                        if j == 0:
                            actionList.append(6)
                        elif j == 1:
                            actionList.append(7)
                        elif j == 2:
                            actionList.append(8)
            return actionList
    
    def undoplay(self, pos: int):
        if pos < 3:
            self.board[0][pos] = "A"
        elif pos > 2 and pos < 6 :
            self.board[1][pos - 3] = "A"
        else:
            self.board[2][pos - 6] = "A"



    def checkWhoWon(self): 
        checker = False             
        #Check for the rows
        for i in range (3):
            if checker == False:
                for j in range (2):
                    checker = self.comparePieces(self.board[i][j], self.board[i][j + 1])
                    who = self.board[i][j]
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
                        who = self.board[i][j]
                        if not checker:
                            break
                else:
                    break


        if checker == False:
            # Check for left to right diagonal
            checker = self.comparePieces(self.board[0][0], self.board[1][1]) and self.comparePieces(self.board[1][1], self.board[2][2])
            who = self.board[0][0]
        if checker == False:
            # Check for right to left diagonal
            checker = checker or (self.comparePieces(self.board[0][2], self.board[1][1]) and self.comparePieces(self.board[1][1], self.board[2][0])) 
            who = self.board[0][2]  
        return who
    
    

    
    
    







    
        
   

        

        

    
    


        





