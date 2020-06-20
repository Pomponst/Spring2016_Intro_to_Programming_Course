In this exercise write a Tweet Tester.

Twitter allows users to send messages of 140 characters or less. Users direct tweets to specific users by using @mentions and label tweets by using #hashtags. Tweets may also contain links that start with http://.

Your code should ask the user to enter a potential tweet. First it will check to see if it is a valid tweet by checking that the length is less than or equal to 140 characters.

If the tweet is too long, your code should print out a message to this effect and the number of characters over 140.

If the tweet is valid, print “Length Correct” and count the number of @mentions, #hashtags and number of links using the following rules:
*	Every @mention will start with the '@' character and have at least one non-space or non-tab character following it.
*	All hashtags will start with the '#' character and have at least one non-space or non-tab character following it.
*	All links will start with the string "http://". Twitter ignores case, so HTTP and http are counted as the same set of characters. You do not need to check for any characters following the http:// .

Note that the space is specified by a space within single or double quotation marks, and that the escape sequence, '\t', can be used to check for a tab character.

Here are two sample interactions. As usual, user input is in bold.

Sample Run 1:

Please enter a tweet:
Please enter a tweet: **This is a #long tweet. An extra long #link. So, when @you write your code it should ignore all of the #hastags and @mentions since it is too long. It should also ignore all http<span></span>://links**
Excess characters: 45

Sample Run 2:

Please enter a tweet: **This #tweet is #short and has @ several #hashtags. And http<span></span>://links @and @mentions #**
Length within limit. No. characters: 85
Number of Hashtags: 3
Number of Attributions: 2
Number of Links: 1

You may of course simply copy these sample tweets into your program’s prompt as opposed to having to re-type them in.
