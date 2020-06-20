#Assignment 8
1. A palindrome is any sequence of characters that reads the same backwards as forwards. One-word examples include:<br>
	Dad	madam	rotor<br>
	Kayak	redder	noon

	For the sake of this exercise, the following may also be considered one-word palindromes:

	1881	zap4554paz

	That is, numeric strings and “nonsense” strings that read the same backwards as forwards should be classified as palindromes.

	Write a program that takes as input a string and determines if it’s a one-word palindrome.  Here’s a sample output.

	Please enter a string: **redder**<br>
	redder is a palindrome.

	Please enter a string: **zap4554paz**<br>
	zap4554paz is a palindrome.

	Please enter a string: **hello**<br>
	hello is not a palindrome.

	Note: Palindromes can be more complicated. The below are considered palindromes too – punctuation, capitalization and spaces are ignored.

	A man, a plan, a canal: Panama!<br>
	Was it a car or a cat I saw?<br>
	No ‘x’ in Nixon<br>
	Ah, Satan sees Natasha!

	Your code does NOT have to handle these. That is, you can presume that all input will have letters of the same case, no blanks, and no punctuation marks.

2. For the following questions, presume the list in question is named lst1.
	1. Write two expressions that return the last item in the list. (So the first expression you provide should return the last item in lst1. The second expression, separately, should also return the last item in lst1.)
	2. Write two expressions that return the first item (that is, the item at index 0) in the list.
	3. Write four expressions that return all but the last three items in the list. (You may presume there are at least three items in the list.)
	4. Write two expressions that return the first, third, fifth etc. items (that is, those items at indexes 0, 2, 4, etc.) of the list.
	5. Write two expressions that return the second, fourth, sixth etc. items (that is, those elements at indexes 1, 3, 5, etc.) of the list.

4. Write a program that takes a string as input, checks to see if it is comprised entirely of letters, and if all those letters are lower case. The output should be one of three possible messages:

	Your string is comprised entirely of lower case letter.<br>
	Your string is comprised entirely of letters but some or all are upper case.<br>
	Your string is not comprised entirely of letters.

	Your program may NOT:
	*	Use an elif.
	*	Test for equality anywhere – that is, you may not use the == symbol.
