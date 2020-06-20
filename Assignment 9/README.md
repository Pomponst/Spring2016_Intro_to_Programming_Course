# Assignment 9
1. Write a program that creates a conversion table for gallons to liters.  The program should display gallons from a starting value provided by the user up to (and including) an ending value provided by the user, in increments specified by the user. Use the relationship that 1 gallon of liquid is equivalent to 3.785 liters.  Two sample program interactions follow. As usual, user input is in bold.

	Enter the starting value: **2**<br>
	Enter the ending value: **6**<br>
	Enter the increment: **1**
	```
	Gallons		Liters
	2.0 		 7.57
	3.0 		 11.36
	4.0 		 15.14
	5.0 		 18.93
	6.0 		 22.71
	```

	Enter the starting value: **.5**<br>
	Enter the ending value: **4**<br>
	Enter the increment: **.5**
	```
	Gallons		Liters
	0.5 		 1.89
	1.0 		 3.79
	1.5 		 5.68
	2.0 		 7.57
	2.5 		 9.46
	3.0 		 11.36
	3.5 		 13.25
	4.0 		 15.14
	```
	In terms of formatting, note the heading (“Gallons” and “Liters”), that the heading and the data are aligned, and that the liters are rounded to two decimal places.
	
2. A machine purchased for $28,000 is depreciated at a rate of $4,000 a year for seven years.  Write a program that computes and displays a depreciation table for seven years.  The table should have the following form (where “EOY Value” stands for “End of Year Value” and “Acc. Dep.” stands for “Accumulated Depreciation”:
	```
	Year	Depreciation	EOY Value	Acc.Dep.
	----	------------	---------	--------
	1 	 4000 		 24000 		 4000
	2 	 4000 		 20000 		 8000
	3 	 4000 		 16000 		 12000
	4 	 4000 		 12000 		 16000
	5 	 4000 		 8000 		 20000
	6 	 4000 		 4000 		 24000
	7 	 4000 		 0 		 28000
	```
	
	3. Write a program to calculate the GPA for a student. The user should specify the number of courses for a particular run, and then the grade and number of credits for each course.  Grades should be entered in numeric format. A table providing these values for each letter grade is provided below.

	|Grade|Points|
	|-----|------|
	|A|4|
	|A-|3.66|
	|B+|3.33|
	|B|3|
	|B-|2.66|
	|C+|2.33|
	|C|2|
	|C-|1.66|
	|D+|1.33|
	|D|1|
	|F|0|

	If you’re not sure how to calculate a GPA, Google it.

	A sample interaction is provided below.

	Enter the number of courses: **4**

	Enter the grade for course 1: **3.33**<br>
	Enter the number of credits for course 1: **3**

	Enter the grade for course 2: **4**<br>
	Enter the number of credits for course 2: **3**

	Enter the grade for course 3: **3**<br>
	Enter the number of credits for course 3: **3**

	Enter the grade for course 4: **3.66**<br>
	Enter the number of credits for course 4: **4**


	Your GPA is: 3.51

	If you can’t get the prompts to specify the course number, just provide simple prompts for the grade and the credits.
