##Variables
total = 0
counter = 1
go = True

##Logic
while go:
    grade = float(input("Enter grade "+str(counter)+": "))
    total = total + grade
    cont = str(input("Do you want to enter another grade (y/n)?"))
    counter = counter + 1
    if cont == "n":
        go = False
        print("Your average grade is:",total/(counter-1))
