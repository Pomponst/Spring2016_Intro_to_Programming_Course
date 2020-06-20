##Input

sales = float(input("What were your monthly sales? "))

##Logic
if sales >=50000:
    income = round(375 + (0.16*sales),2)
    print("Your income this month is $",income)
elif sales>=40000:
    income = round(350 + (0.14*sales),2)
    print("Your income this month is $",income)
elif sales>=30000:
    income = round(325 + (0.12*sales),2)
    print("Your income this month is $",income)
elif sales>=20000:
    income = round(300 + (0.09*sales),2)
    print("Your income this month is $",income)
elif sales>=10000:
    income = round(250 + (0.05*sales),2)
    print("Your income this month is $",income)
elif sales<10000:
    income = round(200 + (0.03*sales),2)
    print("Your income this month is $",income)
