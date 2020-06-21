# Assignment 5
1) Write a program that calculates the monthly income of a salesperson by using the following commission schedule.

	|Monthly Sales|Income|
	|-------------|------|
	|greater than or equal to $50,000|$375 plus 16% of sales|
	|less than $50,000 but greater than or equal to $40,000|$350 plus 14% of sales|
	|less than $40,000 but greater than or equal to $30,000|$325 plus 12% of sales|
	|less than $30,000 but greater than or equal to $20,000|$300 plus 9% of sales|
	|less than $20,000 but greater than or equal to $10,000|$250 plus 5% of sales|
	|less than $10,000|$200 plus 3% of sales|

	Input to the program should be monthly sales (in dollars) and output should be the corresponding income (in dollars).  A sample program interaction follows.  (As usual, user input is in bold.)
	<pre>
	What were your monthly sales? <b>43256</b>
	Your income this month is $ 6405.84</pre>

2. Write a program that asks the user for their marital status: user input should be as follows:

	s – for single<br>
	m – married<br>
	d – divorced<br>
	w – widowed.

	The program’s output should simply be a sentence stating their marital status.  A sample output follows.  As usual, user input is in bold.
	<pre>
	What is your marital status?  <b>m</b>
	You are married.</pre>

	If the user enters some character other than s, m, d or w, the system should respond with the sentence, “You have entered an unrecognizable marital status.”
	
3. Write a program that evaluates a basketball player’s performance. The evaluation will rank a player as either excellent, good, fair or poor. 

	The rank of the player will depend on a system that rates the player’s scoring and rebounding statistics based on the position they play.

	The system assigns rating points as follows:
	|Position|Average Scoring/Game|Average Scoring/Game|
	|--------|--------------------|--------------------|
	|Guard|5.1|1.3|
	|Forward|4.2|2.2|
	|Center|3.1|3.3|

	Example: a forward who scores 13 points per game and 6 rebounds per game will get<br>
		(4.2 * 13) + (2.2 * 6) rating points

	The ranking will depend on rating points as follows:
	|Rating Points|Rating|
	|-------------|------|
	|>= 100|Excellent|
	|>= 85|Good|
	|>= 70|Fair|
	|< 70|Poor|

Your program should prompt the user for the player’s position. (Use the character ‘g’ for guard, ‘f’ for forward and ‘c’ for center.)  Then prompt the user for scoring and rebounding averages. Your program should then print one of the four ratings.
