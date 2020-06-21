# Assginment 11
1. Improve the functionality of the (first) NumberOfVowels program from class to also print out the locations (indexes) of the vowels in the input string. Some sample interactions follow:
	<pre>
	Please enter a string: <b>hello</b>
	The number of vowel occurrences in your string is: 2
	The indexes of the vowels in your string are: [1, 4]</pre>
	<pre>
	Please enter a string: <b>pfft</b>
	The number of vowel occurrences in your string is: 0</pre>
	<pre>
	Please enter a string: <b>bell</b>
	The number of vowel occurrences in your string is: 1<br>
	The index of the vowel in your string is: [1]</pre>
2. Recall the palindrome problem of assignment 8. Write a new program that prompts the user for a string and checks to see if that string is a palindrome. For this updated program, input strings may have punctuation marks, spaces, and capitalizations, but these are ignored in the palindrome check.  Here are some sample interactions.
	<pre>
	Please enter a string to check: <b>A man, a plan, a canal: Panama!</b>
	The string "A man, a plan, a canal: Panama!" is a palindrome.</pre>
	<pre>
	Please enter a string to check: <b>No ‘x’ in Nixon</b>
	The string "No ‘x’ in Nixon" is a palindrome.</pre>
	<pre>
	Please enter a string to check: <b>hello students</b>
	The string "hello students" is not a palindrome.</pre>
3. Write a program that calculates and displays the end of year balances in a savings account if $1,000 is put in the account at 6% interest for five years.  (Recall that if I put $1000 in a bank account at the beginning of the year, then the balance at the end of the year is $1,000 + $1,000*6%.) You may assume no money is removed from the account over this period.<br>
	Your program output should look like this:
	```
	Balance after year 1 is $ 1060.0
	Balance after year 2 is $ 1123.6
	Balance after year 3 is $ 1191.02
	Balance after year 4 is $ 1262.48
	Balance after year 5 is $ 1338.23
	```
	1. Modify your code so that it displays the balances for interest rates from three to five percent inclusive, in one percent intervals.  (Hint: Use an outer loop that iterates on the interest rate, and an inner one that iterates on the year.)
		```
		Interest rate of 3 %:
		Balance after year 1 is $ 1030.0
		Balance after year 2 is $ 1060.9
		Balance after year 3 is $ 1092.73
		Balance after year 4 is $ 1125.51
		Balance after year 5 is $ 1159.27

		Interest rate of 4 %:
		Balance after year 1 is $ 1040.0
		Balance after year 2 is $ 1081.6
		Balance after year 3 is $ 1124.86
		Balance after year 4 is $ 1169.86
		Balance after year 5 is $ 1216.65

		Interest rate of 5 %:
		Balance after year 1 is $ 1050.0
		Balance after year 2 is $ 1102.5
		Balance after year 3 is $ 1157.62
		Balance after year 4 is $ 1215.51
		Balance after year 5 is $ 1276.28
		```
	2. Modify your code to take as input from the user the starting balance, the starting and ending interest rates, and the number of years the money is in the account.
	3. Modify your code (from part c) so that the program only prints out the balance at the end of the last year the money is in the account. (That is, don’t print out the balance during the intervening years.)<br>
	Given the same inputs as in part i, the output for this program would be:
		```
		Interest rate of 3 %:
		Balance after year 5 is $ 1159.27

		Interest rate of 4 %:
		Balance after year 5 is $ 1216.65

		Interest rate of 5 %:
		Balance after year 5 is $ 1276.28
		```
