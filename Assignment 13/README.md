# Assignment 13
1. Write a function called multIt() that takes two numbers as parameters and returns their product.  Write a main() function that prompts the user for the numbers, and prints out the product as calculated by multIt(). Test your code to make sure it works correctly.
2. We started this problem in class. Modify the program from the last assignment that calculates the weekly pay for workers so that:
	1. The called function that calculates the weekly pay for each worker does not print out this value but rather returns it to main(). 
	2. Each user input is done in a called function. (User inputs: number of workers, hourly rate for each worker, and number of hours worked for each worker.) Each of these functions should return the value it gets from the user to main(). Don’t worry about data validation yet. Test your code and make sure it works.
	3. Now update each called function that takes user input to do data validation.  (Don’t worry much about the specifics of what constitutes a legal value in each of these cases. Use anything reasonable, like the number of hours worked must be greater than zero and less than 60.) 
	4. The main() function (not the called function that calculates the weekly pay for each worker) should print out the weekly pay for each worker.
	5. The main() function should also calculate and print out the total payroll for the week.
