# Assignment 14
Implement the following program for playing the game of heads/tails. The rules of the game are as follows:
1.	The computer will ask the player to call heads or tails.
2.	The computer will simulate the flip of a coin.
3.	If the outcome of the flip matches the guess, the player wins otherwise the computer wins the game.

Your program should first print out the rules of the game. Then it should get the number of games the player wishes to play.  For each game, the program should get the player's guess and simulate a coin toss. It should display who won the game.  At the end of all the games, the program should print out a summary of the number of games won by the player, the total number of games played, and the percentage of flips won by the player.

Implement this game using functions that do the following. 
1.	Display the rules of the game **and** get from the player the number of games to play.
2.	Prompt for and read the user's guess.
3.	Simulate the tossing of a coin. 
4.	Display a summary of all games played.

After each flip the program should indicate the result of the flip and if the user guessed correctly or not.

As usual, your program should check all user input to make sure it’s valid (and not let the user proceed until valid input has been entered).

Sample Interaction:
```
See if you can predict if the computer flips heads or tails.
How many times do you want to play? 3

Enter your guess. 0 for tails or 1 for heads: 1
The flip is tails.
Sorry. That's not correct.

Enter your guess. 0 for tails or 1 for heads: 1
The flip is tails.
Sorry. That's not correct.

Enter your guess. 0 for tails or 1 for heads: 1
The flip is heads.
Correct guess.

The coins was flipped 3 times.
You guessed correctly 1 time(s).
Your percentage correct is: 33.33 %.
```
