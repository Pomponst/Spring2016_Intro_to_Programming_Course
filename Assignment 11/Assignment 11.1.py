##Variables
count = 0
lst1 = []

##Input
str1 = str(input("Please enter a string: "))

##Logic
for ch in str1.lower():
    if ch in "aeiou":
        count += 1
        index = str1.index(ch)
        lst1.append(index)

##Calculation        
print("The number of vowel occurences in your sting is:",count)
if lst1 != []:
    print("The index of the vowel in your string is:",lst1)
