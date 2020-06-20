##Input
position = str(input("What is your position?"))
score = float(input("What is your scoring average?"))
rebound = float(input("What is your rebound average?"))

##Logic
if position.lower() == "g":
    performance = (5.1*score)+(1.3*rebound)
elif position.lower() == "f":
    performance = (4.2*score)+(2.2*rebound)
elif position.lower() == "c":
    performance = (3.1*score)+(3.3*rebound) 

if performance >=100:
    print("Rating: Excellent")
elif performance >=85:
    print("Rating: Good")
elif performance >=70:
    print("Rating: Fair")
elif performance <70:
    print("Rating: Poor")
