
from board import Tictactoe 
from ai import Ai
# from player import Player  

def main():
    # print("Who dares Play against the Tic God")
    # print("Prepare to lose mortal")
    # input1  =  input("Enter 1 to start Game, 2 to quit: ")
    # if input == 1:
    #     board1 = Tictactoe()
    #     board1.printBoard()
    #     player = Player(board1)
    #     ai =  Ai(board1)
    #     while board1.gameOver == False:
    #         input2 = input("Your move mortal")
    #         board1.play(input2, "X")
    #         ai.minmax()

    






    board1 = Tictactoe()
    # board1.printBoard()
    board1.play(0,"X")
    board1.play(1,"O")
    board1.play(2,"X")
    board1.play(3,"O")
    board1.play(4,"X")
    board1.play(5,"X")
    board1.play(6,"O")
    board1.play(7,"A")
    board1.play(8,"O")
    board1.printBoard()
    ai = Ai(board1)
    print("The value of the minimax is",ai.MiniMax())



    
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