## Input
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))
grade5 = float(input("Enter the fifth grade: "))

## List
grades = [grade1, grade2, grade3, grade4, grade5]

##Caluclations
print("The grades are: ",grades)
low = (sorted(grades))
print("The grades sorted from lowest to highest: ",low)
high = list(reversed(low))
print("The grades sorted from highest to lowest: ",high)

##Logic
min1 = min(grades)
if min1 in grades:
    grades.remove(min1)
min2 = min(grades)
if min2 in grades:
    grades.remove(min2)
average = sum(grades)/len(grades)
print("The average with the two lowest grades removed is: ",average)
