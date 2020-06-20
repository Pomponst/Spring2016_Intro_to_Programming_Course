##Variable
counter = 1
creditList = []
calcList = []

##Input
grade = float(input("Enter the grade for course "+str(counter)+". (Enter -1 to stop.): "))
credit = int(input("Enter the number of credits for course "+str(counter)+": "))

##Logic
while grade >=0:
    creditList.append(credit)
    calc = grade * credit
    calcList.append(calc)
    counter = counter + 1
    grade = float(input("Enter the grade for course "+str(counter)+". (Enter -1 to stop.): "))
    if grade == -1:
        print("Your GPA is: ", round(sum(calcList) / sum(creditList),2))
    else:
        credit = int(input("Enter the number of credits for course "+str(counter)+":"))
