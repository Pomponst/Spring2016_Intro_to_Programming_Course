import random

SIZE = 3

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def assignValues():
    # This function assigns random integer values between 0 and 9 to board
    for r in range(0,SIZE):
        for c in range(0,SIZE):
            board[r][c] = random.randint(0,9)

def printBoard():
    # This function prints out the board
    for r in range(0,SIZE):
        print()
        for c in range(0,SIZE):
            print(board[r][c], end=" ")
    print()

def calcSumRow(r):
    # This function prints out the sum of the elements in row r
    totRow = sum(board[r])
    print("The total of row",r,"is:",totRow)

def calcSumCol(c):
    # This function prints out the sum of the elements in column c
    totCol = sum(i[c] for i in board)
    print("The total of column",c,"is:",totCol)

def calcSumDiag1():
    # This function prints out the sum of the elements in a diaganol from top left to bottom right
    # totDiag1 = board[0][0] + board[1][1] + board[2][2]
    totDiag1 = 0
    for i in range(0,SIZE):
        totDiag1 += board[i][i]
    print("The total of the diaganol from top left to bottom right is:",totDiag1)

def calcSumDiag2():
    # This function prints out the sum of the elements in a diaganol from top right to bottom left
    # totDiag1 = board[0][2] + board[1][1] + board[2][0]
    totDiag2 = 0
    for i in range(0,SIZE):
        totDiag2 += board[i][SIZE-1-i]
    print("The total of the diaganol from top right to bottom left is:",totDiag2)

def main():
    print("Printing initial board:")
    printBoard()
    assignValues()
    print("\nPrinting board after random values have been assigned:")
    printBoard()
    print()
    for i in range(0,SIZE):
        calcSumRow(i)
        calcSumCol(i)
    calcSumDiag1()
    calcSumDiag2()

main()
