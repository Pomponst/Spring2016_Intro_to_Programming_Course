# Assignment 15
1. Recall that Python provides built-in functions to switch back and forth between characters and the numeric values used to represent them:

	\>>> ord('A')<br>
	65<br>
	\>>> chr(65)<br>
	'A'

	The number 65 here is the Unicode representation of the upper case letter A. 

	Write a program that “decodes” the following input string of Unicode values. 

	76 105 118 101 32 108 111 110 103 32 97 110 100 32 112 114 111 115 112 101 114 46

	That is, your program should print out the equivalent of the input in characters.

	Here’s a sample interaction using a different string of Unicode.
	<pre>
	Enter the coded message: <b>71 111 32 80 105 114 97 116 101 115 33</b>
	The decoded message is: Go Pirates!</pre>
2. Revise your code to both encode and decode messages. Here are three sample runs of the code.
	
	*Run 1:*
	<pre>
	Enter 1 to encode a character string into Unicode.
	Enter 2 to decode a Unicode string into characters.
	Choice: <b>1</b>
	Enter the character string to encode: <b>Happy April Fool's Day!</b>
	The encoded message is: 72 97 112 112 121 32 65 112 114 105 108 32 70 111 111 108 39 115 32 68 97 121 33</pre>
	*Run 2:*
	<pre>
	Enter 1 to encode a character string into Unicode.
	Enter 2 to decode a Unicode string into characters.
	Choice: <b>2</b>
	Enter the Unicode string to decode: <b>76 105 118 101 32 108 111 110 103 32 97 110 100 32 112 114 111 115 112 101 114 46</b>
	The decoded message is: Live long and prosper.</pre>
	*Run 3:*
	<pre>
	Enter 1 to encode a character string into Unicode.
	Enter 2 to decode a Unicode string into characters.
	Choice: <b>3</b>
	Invalid choice. Please try again.
	Enter 1 to encode a character string into Unicode.
	Enter 2 to decode a Unicode string into characters.
	Choice: <b>5</b>
	Invalid choice. Please try again.
	Enter 1 to encode a character string into Unicode.
	Enter 2 to decode a Unicode string into characters.
	Choice: <b>2</b>
	Enter the Unicode string to decode: <b>71 111 32 80 105 114 97 116 101 115 33</b>
	The decoded message is: Go Pirates!</pre>
	Guidelines<br>
	As usual, use good modular design. You should have separate called functions to get Choice from the user, to encode a character string and to decode a Unicode string. Your program does not have to do any input data validation on the user-entered strings that are to be encoded/decoded.

	The main() function should call the choice function, take the string input from the user (either character or Unicode), and print out the encoded or decoded messages. Your function that encodes the character string should return the coded message as a list to main(). Your function that decodes the Unicode string should return the decoded message as a string to main().
	
3. Write a program that takes as input a date in the mm/dd/yyyy format and outputs the date in the *month day, year* format. 

	Two sample interactions follow.

	<pre>
	Enter a date (mm/dd/yyyy): <b>04/01/2016</b>
	The converted date is: April 01, 2016</pre>
	<pre>
	Enter a date (mm/dd/yyyy): <b>7/4/2015</b>
	The converted date is: July 4, 2015</pre>
	Note that in the second interaction, the user entered the month and date as single digits. Your code should be able to accommodate this.

	Your main() function should get input from the user, and call a function to extract the month, date and year as strings from the input. This called function should return these three values to main() which then should do the remainder of the tasks.

