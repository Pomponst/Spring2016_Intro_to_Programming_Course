##Input
hours = float(input("How many hours do you work in a given week?"))
wage = float(input("What is your hourly wage?"))

##Logic
if hours>40:
    grossPay = (wage*40)+((wage*1.5)*(hours-40))
else:
    grossPay = wage*hours

##Calculation
print("Your gross pay is: $",grossPay)
