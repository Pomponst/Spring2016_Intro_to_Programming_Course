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
	```
	Enter the coded message: 71 111 32 80 105 114 97 116 101 115 33
	The decoded message is: Go Pirates!
	```
