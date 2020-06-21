# Assignment 10
1. Re-write the GPA problem from Assignemnt 9, this time including data validation for all input data.
2. Re-write the GPA problem from Assignment 9, this time using a sentinel value to stop input.  That is, the user should NOT be prompted for the number of courses, but processing additional courses should stop and the GPA outputted when the user inputs the sentinel value.  A sample interaction follows.
	<pre>
	Enter the grade for course 1. (Enter -1 to stop.): <b>4</b>
	Enter the number of credits for course 1: <b>3</b>

	Enter the grade for course 2. (Enter -1 to stop.): <b>3</b>
	Enter the number of credits for course 2: <b>3</b>

	Enter the grade for course 3. (Enter -1 to stop.): <b>3.5</b>
	Enter the number of credits for course 3: <b>2</b>

	Enter the grade for course 4. (Enter -1 to stop.): <b>-1</b>

	Your GPA is: 3.5</pre>

	Note: You may do this problem without data validation.
	
3. Often the user is simply prompted to see if s/he wants the program to “go again.” Consider the following interaction for the average grades program:
	<pre>
	Enter grade 1: <b>70</b>
	Do you want to enter another grade (y/n)? <b>y</b>
	Enter grade 2: <b>80</b>
	Do you want to enter another grade (y/n)? <b>y</b>
	Enter grade 3: <b>90</b>
	Do you want to enter another grade (y/n)? <b>n</b>
	The average grade is: 80.0</pre>

	Your code may assume that the user will enter at least one grade. You do not have to worry about input data validation, but you may deal with it if you want to. (Get the program working correctly without it first.)
