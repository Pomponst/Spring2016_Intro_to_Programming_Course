import random
printBoard = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
playBoard = [[0,0,0],
             [0,0,0],
             [0,0,0]]
def printInfo():
    ##This function prints out the game's instructions
    print("Welcome to Tic-Tac-Toe.  You will play x and the computer will play o.  After you move, the computer will move and then display the current board.")
    
def printGame():
    ##This function prints out the playing board with x's and o's
    for row in range(0,3):
        print()
        for col in range(0,3):
            print (printBoard[row][col], end=" ")
    print()
def calcSumRow(row):
    ##This function calculates the sum of the elements in row row
    sumRow = sum(playBoard[row])
    return sumRow
        
def calcSumCol(col):
    ##This function calculates the sum of the elements in column col
    sumCol=0
    for r in range(0,3):
        sumCol+=playBoard[r][col]
    return sumCol

def calcSumDiagLR():
    ##This function calculates the sum of element diag from L to R
    sumDiagLR = 0
    for rc in range(0,3):
        sumDiagLR+=playBoard[rc][rc]
    return sumDiagLR

def calcSumDiagRL():
    ##This function calculates the sum of element diag from R to L
    sumDiagRL = 0
    for r in range(0,3):
        sumDiagRL+=playBoard[r][2-r]
    return sumDiagRL

def playerMove():
    ##This functions is how the player will make a move
    print("Your move")
    r = int(input("Enter row: "))
    c = int(input("Enter column: "))
    while playBoard[r][c] in (1,-1):
        print("There is already a peace there, try again.")
        r = int(input("Enter row: "))
        c = int(input("Enter column: "))
    playBoard[r][c] = 1
    printBoard[r][c] = "x"

def checkGameOver():
    ##This function checks if the game is over
    sums = [calcSumRow(0),calcSumRow(1),calcSumRow(2),calcSumCol(0),calcSumCol(1),calcSumCol(2),calcSumDiagLR(),calcSumDiagRL()]
    if -3 in sums:
        print("Computer wins.")
    elif 3 in sums:
        print("You win!")
    elif drawTest():
        print("Draw!")
    else:
        return "notOver"

def drawTest():
    ##This function will check if there is a draw for the checkGameOver function
    total = 0
    for row in range(0,3):
        for col in range(0,3):
            if playBoard[row][col] == 0:
                total += 1
    if total == 0:
        return "true"

def computerMove():
    ##This function governs how the computer moves
    if calcSumRow(0) in (-2,2):
        r=0
        if playBoard[r][0] == 0:
            c = 0
        elif playBoard[r][1] == 0:
            c = 1
        elif playBoard[r][2] == 0:
            c = 2
    elif calcSumRow(1) in (-2,2):
        r=1
        if playBoard[r][0] == 0:
            c = 0
        elif playBoard[r][1] == 0:
            c = 1
        elif playBoard[r][2] == 0:
            c = 2        
    elif calcSumRow(2) in (-2,2):
        r=2
        if playBoard[r][0] == 0:
            c = 0
        elif playBoard[r][1] == 0:
            c = 1
        elif playBoard[r][2] == 0:
            c = 2
    elif calcSumCol(0) in (-2,2):
        c=0
        if playBoard[0][c] == 0:
            r = 0
        elif playBoard[1][c] == 0:
            r = 1
        elif playBoard[2][c] == 0:
            r = 2
    elif calcSumCol(1) in (-2,2):
        c=1
        if playBoard[0][c] == 0:
            r = 0
        elif playBoard[1][c] == 0:
            r = 1
        elif playBoard[2][c] == 0:
            r = 2
    elif calcSumCol(2) in (-2,2):
        c=2
        if playBoard[0][c] == 0:
            r = 0
        elif playBoard[1][c] == 0:
            r = 1
        elif playBoard[2][c] == 0:
            r = 2
    elif calcSumDiagLR() in (-2,2):
        if playBoard[0][0] == 0:
            r=0
            c=0
        elif playBoard[1][1] == 0:
            r=1
            c=1
        elif playBoard[2][2]:
            r=2
            c=2
    elif calcSumDiagRL() in (-2,2):
        if playBoard[0][2] == 0:
            r=0
            c=2
        elif playBoard[1][1] == 0:
            r=1
            c=1
        elif playBoard[2][0]:
            r=2
            c=0
    else:
        r = random.randint(0,2)
        c = random.randint(0,2)
        while playBoard[r][c] in (1,-1):
            r = random.randint(0,2)
            c = random.randint(0,2)
    playBoard[r][c] = -1
    printBoard[r][c] = "o"
    
def main():
    printInfo()
    printGame()
    while checkGameOver() == "notOver":
        playerMove()
        if checkGameOver() == "notOver":
            computerMove()
        printGame()

main()
