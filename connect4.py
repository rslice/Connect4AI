#Rules:
# 7 Wide - 6 High
# You can only stack above another chip
# 4 in a row wins

import numpy as np

freshBoard = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]])

row = 5
rows = 0
cols = 0

def printBoard():
    for cols in range (0, 7) :
            print(cols+1, end= ' ')
    
    for rows in range(0, 6) :
        print(' ')
        for cols in range (0, 7) :
            print(freshBoard[rows, cols], end= ' ')
    print(' ')
    print(' ')


def placeMove(playerNumber, column):
    movePlaced = False
    row = 5

    while (movePlaced == False):
        if (row == 0 and freshBoard[row, column-1] != 0):
            print("Invalid move")
            colVal3 = input("Enter your move Player " + str(playerNumber) + ": ")
            placeMove(playerNumber, int(colVal3))
            if (winningMove(int(colVal3), playerNumber) == True):
                gameEnd = True
            movePlaced = True
            
            #Is valid location

        elif(freshBoard[row, column-1] != 0):
            row -= 1    
        elif(freshBoard[row, column-1] == 0):
            movePlaced = True
            freshBoard[row, column-1] = playerNumber

    printBoard()

def inputMoves():
    gameEnd = False
    while (gameEnd != True):
        colVal1 = input("Enter your move Player 1: ")
        placeMove(1, int(colVal1))
        if (winningMove(int(colVal1), 1) == True):
            gameEnd = True
        if (gameEnd != True):
            colVal2 = input("Enter your move Player 2: ")
            placeMove(2, int(colVal2))
            if (winningMove(int(colVal2), 2) == True):
                gameEnd = True
    print ("GAME WON")
           
def winningMove(previousCol, piece):
    # Check horizontal locations for win
    for c in range(4):
	    for r in range(6):
		    if freshBoard[r][c] == piece and freshBoard[r][c+1] == piece and freshBoard[r][c+2] == piece and freshBoard[r][c+3] == piece:
			    return True

	# Check vertical locations for win
    for c in range(7):
	    for r in range(3):
		    if freshBoard[r][c] == piece and freshBoard[r+1][c] == piece and freshBoard[r+2][c] == piece and freshBoard[r+3][c] == piece:
			    return True

	# Check positively sloped diagonals
    for c in range(4):
	    for r in range(3):
		    if freshBoard[r][c] == piece and freshBoard[r+1][c+1] == piece and freshBoard[r+2][c+2] == piece and freshBoard[r+3][c+3] == piece:
			    return True

	# Check negatively sloped diagonals
    for c in range(4):
	    for r in range(3, 6):
		    if freshBoard[r][c] == piece and freshBoard[r-1][c+1] == piece and freshBoard[r-2][c+2] == piece and freshBoard[r-3][c+3] == piece:
			    return True
    
    
inputMoves()
