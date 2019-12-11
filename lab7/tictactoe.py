# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Tom Magnusson
# Created: 2019-10-29

symbol = [ " ", "x", "o" ]

# TODO: emphasize difference between logic and presentation
# e.g. "renderRow" (string) vs. "printRow" (side effect printing)

def printRow(row):
    rowStr = [symbol[s] for s in row]
    print(f"| {' | '.join(rowStr)} | ")

# TODO: instructions say use string concatenation
# But comments say to directly print
def printBoard(board):
    border = "+-----------+"
    print(border)
    for row in board:
        printRow(row)
        print(border)
    pass

# TODO: mutating input as side effect-ey output... good place to introduce notion of `pure` function (students love using global variables)
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    if(board[row][col] == 0):
        board[row][col] = player
        return True

    return False

def getPlayerMove():
    row = input("Pick a row:")
    col = input("Pick a column:") 
    return (int(row), int(col)) # then return that row and column instead of (0,0)

def hasBlanks(board):
    for row in board:
        for square in row:
            if square == 0:
                return True
    return False

def determineConsecutiveSquaresWinner(consecutiveSquares):
    if consecutiveSquares == [1,1,1]:
        return 1
    if consecutiveSquares == [2,2,2]:
        return 2
    return 0

def determineWinner(board):
    winner = 0
    for row in board:
        winner = determineConsecutiveSquaresWinner(row)
        if not winner == 0:
            return winner
    
    for i in range(3):
        winner = determineConsecutiveSquaresWinner([board[j][i] for j in range(3)])
        if not winner == 0:
            return winner

    winner = determineConsecutiveSquaresWinner([board[i][i] for i in range(3)])
    if not winner == 0:
        return winner
    
    winner = determineConsecutiveSquaresWinner([board[2][0], board[1][1], board[0][2]])

    return winner


def main():
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        winner = determineWinner(board)
        if(not winner == 0):
            printBoard(board)
            print(f"Congratulations player {winner}, you win!")
            break
        player = player % 2 + 1 # switch player for next turn

if __name__ == "__main__":
    main()
