## Input
str1 = input("Enter a string: ")

## Calculation
str1 = str1.casefold()
rev_str = reversed(str1)

## Logic
if list(str1) == list(rev_str):
   print(str1,"is palindrome")
else:
   print(str1,"is not palindrome")
