##Input
numbers = str(input("Please enter three numbers (seperated by spaces):"))
number1, number2, number3 = numbers.split(" ")

##Logic
if float(number1) > float(number2):
    if float(number1) > float(number3):
        greatest=(number1)
    
if float(number2) > float(number1):
    if float(number2) > float(number3):
        greatest=(number2)
    
if float(number3) > float(number2):
    if float(number3) > float(number1):
        greatest=(number3)

##Calculation
print("The largest number is:",greatest)
