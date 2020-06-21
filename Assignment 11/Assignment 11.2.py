##Input
import re
inpt = input(str("Please enter a string: "))

##Calculation
str1 = inpt
str1 = str1.lower()
str1 = re.sub("\W","",str1)
rvrs = str1[::-1]

##Logic
if str1 == rvrs:
    print(inpt,"is a palindrome.")
else:
    print(inpt,"is not a palindrome.")
