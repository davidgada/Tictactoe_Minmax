
from board import Tictactoe 

def main():
    print("Main file is")
    board1 = Tictactoe()
    board1.printBoard()

    board1.play(0,"O")
    board1.play(1,"A")
    board1.play(2,"O")
    board1.play(3,"X")
    board1.play(4,"O")
    board1.play(5,"X")
    board1.play(6,"X")
    board1.play(7,"A")
    board1.play(8,"X")
    board1.printBoard()

    if board1.checkWinner() == True:
        print("Winning play")
    else:
        print("Losing stuff")

    if board1.checkDraw() == True:
        print("Draw")
    else:
        print("Not Draw")


main()