##Input
num = int(input("Enter the number of courses: "))
while num <=0:
    print("The number of grades must be greater than zero. Try again>")
    num = int(input("Enter the number of courses: "))
print("\n")

##Variable
counter = 1
creditList = []
calcList = []

##Logic
while counter <= num:
    grade = float(input("Enter the grade for course "+str(counter)+": "))
    while grade <0 or grade >4:
        print("The grade must be between zero and 4. Please try again")
        grade = float(input("Enter the grade for course "+str(counter)+": "))
    credit = int(input("Enter the number of credits for course "+str(counter)+":"))
    while credit <=0:
        print("The number of credits must be greater than zero")
        credit = int(input("Enter the number of credits for course:"))
    print("\n")
    creditList.append(credit)
    calc = grade * credit
    calcList.append(calc)
    counter = counter + 1

##Calculation
print("Your GPA is: ", round(sum(calcList) / sum(creditList),2))
