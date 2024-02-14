
from board import Tictactoe 

def main():
    print("Main file is")
    board1 = Tictactoe()
    board1.printBoard()

    board1.play(0,"X")
    board1.play(1,"X")
    board1.play(2,"X")
    board1.printBoard()

    if board1.checkWinner() == True:
        print("Winning play")
    else:
        print("Losing stuff")


main()