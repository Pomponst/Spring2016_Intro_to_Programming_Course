# Assignment 17
Write the pseudocode for a program that allows a person to play a new type of lottery.  The rules of the lottery game are as follows.

The player guesses a number between 1 and 99. The computer simulates spinning a wheel that will yield a number between 1 and 99.

If the player's guess matches the wheel then they are paid the larger of $2,500 or $50 times the number guessed.  So, for example, if the number was 90 then the payoff is $4,500; if the number was 10 then the payoff is $2,500.

If the player's guess was within 25 (i.e. plus or minus 25) of the number, then they have a choice: they can receive $750, or have the wheel re-spun and get $20 times the number on the second spin. Your program should ask the player for their choice. See the example below.

If the player's guess was outside of 25 they get nothing.

Your pseudocode for the program should go include all the interaction described above and print out the result of each game and the total for all games. Also, it should allow the player to indicate at the start how many games they wish to play.

The following is a sample run of the game.  As usual, user input is in bold.
```
Please enter the number of games you wish to play? 3

Enter your guess. 30
The wheel landed on 30.
You win $2500.

Enter your guess. 20
The wheel landed on 15
Do you wish to spin the wheel for your prize (y/n)? y
The wheel landed on 40.
You win $800.

Enter your guess. 113
Invalid guess
Enter your guess. 75
The wheel landed on 50.
You lose.

Your total for 3 games is $3300.
```
Again, you should not write the program, just the pseudocode.
