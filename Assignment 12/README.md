1. Write a program that prints out a deck of cards, in the format specified below. (That is, the following should be the output of your code).
	```
	2 of hearts	2 of diamonds	2 of spades	2 of clubs
	3 of hearts	3 of diamonds	3 of spades	3 of clubs
	4 of hearts	4 of diamonds	4 of spades	4 of clubs
	5 of hearts	5 of diamonds	5 of spades	5 of clubs
	6 of hearts	6 of diamonds	6 of spades	6 of clubs
	7 of hearts	7 of diamonds	7 of spades	7 of clubs
	8 of hearts	8 of diamonds	8 of spades	8 of clubs
	9 of hearts	9 of diamonds	9 of spades	9 of clubs
	10 of hearts	10 of diamonds	10 of spades	10 of clubs
	J of hearts	J of diamonds	J of spades	J of clubs
	Q of hearts	Q of diamonds	Q of spades	Q of clubs
	K of hearts	K of diamonds	K of spades	K of clubs
	A of hearts	A of diamonds	A of spades	A of clubs
	```
	Start your program by defining the following two lists.
	```
	suits = ["hearts", "diamonds", "spades", "clubs"]
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	```
2. Write a program that determines the average exam grade for each student in a course. The program should prompt the user for the number of students and the number of exams. Here’s a sample interaction:
	<pre>
	How many students? <b>2</b>
	How many exams? <b>3</b>
	Enter the score for student 1 for exam 1: <b>70</b>
	Enter the score for student 1 for exam 2: <b>80</b>
	Enter the score for student 1 for exam 3: <b>90</b>
	The average exam score for student 1 is: 80.0
	
	Enter the score for student 2 for exam 1: <b>65</b>
	Enter the score for student 2 for exam 2: <b>70</b>
	Enter the score for student 2 for exam 3: <b>85</b>
	The average exam score for student 2 is: 73.33</pre>
	Your code does not have to deal with input data validation.
3. After writing each function below, include the function in a working program and test the function by passing data to it. Paste your entire program in each case in the spaces indicated.<br>
Python comes with many built-in functions including abs() and max(). Your task here is to write functions that duplicate the functionality of these built-in functions (without, of course, using them).
	1. Write a method named findAbs() that accepts a number passed to it, computes its absolute value, and displays the absolute value.  The absolute value of a number is the number itself if the number is positive and is the negative of the number if the number is negative.
	2. Write a method named maxFun() that accepts three numbers passed to it, determines the maximum of the three numbers, and displays this maximum number.
4. Write a program that calculates the weekly pay for workers. The program should contain three functions: main(), printInfo() and calcPay().

	printInfo() simply prints out what the program does. To minimize busywork for you, I’m including the print statements that comprise printInfo() below:

		print ("This program calculates the weekly pay for hourly workers.")
		print ("Workers get \"time and a half\" for overtime.")
		print ("That is, for all hours worked above 40, they get paid at 1.5 times their regular hourly rate.")
		print ("Enter the number of workers for whom pay is to be calculated.")               
		print ("Then, for each worker, enter the hourly pay rate and the number of hours worked.\n")
		
	main() does the following:
	* It calls printInfo().
	* It prompts the user for the number of workers for whom pay is to be calculated.
	* Then for each worker it prompts the user for the hourly pay rate and the hourly wage.
	* It then calls payCalc() for each worker, passing to payCalc() the rate and wage for that worker.
			
	payCalc() determines the weekly wage for a worker and prints out that value.<br>
	Your code does not have to do any input data validation.<br>
	Here's a sample interaction:
	<pre>
	This program calculates the weekly pay for hourly workers.
	Workers get "time and a half" for overtime.
	That is, for all hours worked above 40, they get paid at 1.5 times their regular-hourly rate.
	Enter the number of workers for whom pay is to be calculated.
	Then, for each worker enter the hourly pay rate and the number of hours worked.

	How many workers? <b>3</b>

	Enter the hourly pay rate for worker 1: <b>10</b>
	Enter the number of hours worked for worker 1: <b>35</b>
	This week's pay: $ 350.0

	Enter the hourly pay rate for worker 2: <b>10</b>
	Enter the number of hours worked for worker 2: <b>45</b>
	This week's pay: $ 475.0

	Enter the hourly pay rate for worker 3: <b>12.75</b>
	Enter the number of hours worked for worker 3: <b>42.5</b>
	This week's pay: $ 557.81</pre>
