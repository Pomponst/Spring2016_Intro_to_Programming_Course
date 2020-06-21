# Assignment 18
Write a program that plays tic-tac-toe against a user. The user should play the x’s while the program plays o’s. Allow the user to go first.

The strategy for the program, when it is the programs turn, is to randomly select any available space.

Display the board after each move by the program.

The game is over when either the computer or the user has three spaces in a row (vertical, horizontal or diagonal), or all the spaces are occupied.

Print out the winner or note that it’s a draw at the conclusion of the game.

Here’s a sample interaction.  User input is in bold.  Notice the use of a two dimensional, three-by-three array for the board.  The space in the upper left-hand corner is location 0 0, the location directly below this one is 1 0, etc.
```
Welcome to Tic-Tac-Toe.  You will play x and the computer will play o.  After you move, the computer will move and then display the current board.

Your move
Enter row: 1 
Enter column: 1

 -  -  -
 -  x  -
 -  o  -

Your move
Enter row: 2 
Enter column: 0

 -  -  -
 o  x  -
 x  o  -

Your move
Enter row: 0 
Enter column: 2

 -  -  x
 o  x  -
 x  o  -

Congratulations -- you've won!
```
Extra Credit:<br>
Have the program play more intelligently by
1. Blocking two-in-a-row threats.
2. Making the game-winning move if it has a two-in-a-row threat.
