# Assignment 6
2. Write a program that takes as input five grades and outputs a) the grades that were input and b) the average after dropping the two lowest grades. Do this by placing the input values into a list called grades, and then performing the appropriate calculations/manipulations on the list. Hint: the first line of your code should be this:

	grades = []    # Create the variable grades and assign it the empty list.

	(To the right of the equal sign is an open bracket then closed bracket. This is an empty list.)

	A sample interaction follows. User input is in bold.
	<pre>
	Enter the first grade: <b>95</b>
	Enter the second grade: <b>85</b>
	Enter the third grade: <b>34</b>
	Enter the fourth grade: <b>75</b>
	Enter the fifth grade: <b>22</b>
	The grades are:  [95.0, 85.0, 34.0, 75.0, 22.0]
	The average with the two lowest grades removed is:  85.0</pre>

3. Modify your code so that after printing out the grades as before your program prints out the grades sorted from low to high, and then prints them out from high to low (and then prints out the average as before).  

	A sample interaction follows. User input is in bold.
	<pre>
	Enter the first grade: <b>95</b>
	Enter the second grade: <b>85</b>
	Enter the third grade: <b>34</b>
	Enter the fourth grade: <b>75</b>
	Enter the fifth grade: <b>22</b>
	The grades are:  [95.0, 85.0, 34.0, 75.0, 22.0]
	The grades sorted from lowest to highest:  [22.0, 34.0, 75.0, 85.0, 95.0]
	The grades sorted from highest to lowest:  [95.0, 85.0, 75.0, 34.0, 22.0]
	The average with the two lowest grades removed is:  85.0</pre>
