
from board import Tictactoe 
from ai import Ai
# from player import Player  

def main():
    print("Who dares Play against the Tic God")
    print("Prepare to lose mortal")
    input1  =  int(input("Enter 1 to start Game, 2 to quit: "))
    if input1 == 1:
        board1 = Tictactoe()
        board1.printBoard()
        print("\n")        
        ai =  Ai(board1)
        while board1.gameOver != False:
            input2 = int(input("Your move mortal"))
            board1.play(input2, "X")
            board1.printBoard()
            print("\n")  
            ai.play()
            board1.printBoard()
            print("\n")        


    






    # board1 = Tictactoe()
    # print("Original Board","\n")
    # board1.printBoard()
    # print("Initializing Board with pieces","\n")
    # board1.play(0,"O")
    # board1.play(1,"O")
    # board1.play(2,"X")
    # board1.play(3,"X")
    # board1.play(4,"A")
    # board1.play(5,"X")
    # board1.play(6,"O")
    # board1.play(7,"X")
    # board1.play(8,"O")
    # board1.printBoard()
    # print("Ai plays move now","\n")
    # ai = Ai(board1)
    # ai.play()
    # board1.printBoard()








    # print("The value of the minimax is",ai.MiniMax())
    # if board1.checkDraw() == True:
    #     print("Draw")
    # else:
    #     print("Not Draw")

    # print("Testing the result part of the minmax: \n")
    # (ai.resultState(board1, 7)).printBoard()

    # print("The positions available for input are", board1.actionSpace())
    # print("Testing to see if the board is changed as well \n")

    # board1.printBoard()




    print("\n")



    
    # print("The current player turn is ",board1.checkTurn())
    # print("The positions available for input are", board1.actionSpace())
    # print("The positions available for input are", board1.actionSpace())





    # if board1.checkWinner() == True:
    #     print("Winning play")
    # else:
    #     print("Losing stuff")

    

main()