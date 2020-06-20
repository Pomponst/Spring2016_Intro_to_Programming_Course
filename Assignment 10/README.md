# Assignment 10
1. Re-write the GPA problem from Assignemnt 9, this time including data validation for all input data.
2. Re-write the GPA problem from Assignment 9, this time using a sentinel value to stop input.  That is, the user should NOT be prompted for the number of courses, but processing additional courses should stop and the GPA outputted when the user inputs the sentinel value.  A sample interaction follows.

	Enter the grade for course 1. (Enter -1 to stop.): **4**<br>
	Enter the number of credits for course 1: **3**

	Enter the grade for course 2. (Enter -1 to stop.): **3**<br>
	Enter the number of credits for course 2: **3**

	Enter the grade for course 3. (Enter -1 to stop.): **3.5**<br>
	Enter the number of credits for course 3: **2**

	Enter the grade for course 4. (Enter -1 to stop.): **-1**

	Your GPA is: 3.5

	Note: You may do this problem without data validation.
	
3. Often the user is simply prompted to see if s/he wants the program to “go again.” Consider the following interaction for the average grades program:

	Enter grade 1: **70**<br>
	Do you want to enter another grade (y/n)? **y**<br>
	Enter grade 2: **80**<br>
	Do you want to enter another grade (y/n)? **y**<br>
	Enter grade 3: **90**<br>
	Do you want to enter another grade (y/n)? **n**<br>
	The average grade is: 80.0

	Your code may assume that the user will enter at least one grade. You do not have to worry about input data validation, but you may deal with it if you want to. (Get the program working correctly without it first.)
