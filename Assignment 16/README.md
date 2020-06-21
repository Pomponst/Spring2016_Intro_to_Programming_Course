# Assignment 16
Consider the following nested list.

Board = [[0,0,0],<br>
	 [0,0,0],<br>
	 [0,0,0]]

Write a program that:
1. Creates this list. It should be global in scope.(By “create” I mean simply that this assignment statement should be in your program.)
2. Uses a global constant called SIZE that represents the size of board. Note that board is “square” -that is, it is a two-dimensional nested list with the same number of rows as columns. Therefore, set SIZE equal to 3, the number of rows/columns.
3. Includes the following called functions.
	```
	def assignValues(): # This function assigns random integer values between 0 and 9 (inclusive) to board.(The random values replace the initial values.)
	def printBoard(): # This function prints out board.
	def calcSumRow(r): # This function prints out the sum of the elements in row r, where r is a number specifying the row (that is,0, 1, or 2).
	def calcSumCol(col): # This function prints out the sum of the elements in columncol, where col is a number specifying the column (that is,0, 1, or 2).
	def calcSumDiag1(): #Thisfunction prints out the sum of the elements in the top-left to bottom-rightdiagonal.
	def calcSumDiag2(): #Thisfunction prints out the sum of the elementsin thetop-right to bottom-leftdiagonal.
	def main(): #Thisfunction callstheother functions so that the program prints out as specified.
	```
	So, you should write main so that the program output looks like the sample outputs below.(Your results will be different astheprogram assigns random values to board.)Your program should be written such that if the board size were 100, it would require very few changes to have the same functionality. Submit your work as a Python file.

	*Sample Run 1*
	```
	Printing initial board:
	0   0   0
	0   0   0
	0   0   0
	Printing board after random values have been assigned:
	2   4   3
	3   4   7
	8   5   4
	The total of row 0 is: 9
	The total of column 0 is: 13
	The total of row 1 is: 14
	The totalof column 1 is: 13
	The total of row 2 is: 17
	The total of column 2 is: 14
	The total of the diagonal from top left to bottom right is: 10
	The total of the diagonal from top right to bottom left is: 15
	```
	*Sample Run 2*
	```
	Printing initial board:
	0   0   0
	0   0   0
	0   0   0
	Printing board after random values have been assigned:
	6   8   1
	4   7   7
	5   1   7
	The total of row 0 is: 15
	The total of column 0 is: 15
	The total of row 1 is: 18
	The total of column 1 is: 16
	The total of row 2 is: 13
	The total of column 2 is: 15
	The total of the diagonal from top left to bottom right is: 20
	The total of the diagonal from top right to bottom left is: 13
	```
