def printInfo():
    print("This program calculates the weekly pay for hourly workers.")
    print("Workers get \"time and a half\" for overtime.")
    print ("That is, for all hours worked above 40, they get paid at 1.5 times their regular hourly rate.")
    print ("Enter the number of workers for whom pay is to be calculated.")               
    print ("Then, for each worker, enter the hourly pay rate and the number of hours worked.\n")

def calcPay (rate, hours):
    if hours <=40:
        pay = rate*hours
    else:
        pay = rate*40 + (hours-40)*rate*1.5
    return pay

def getNumWorkers():
    numWorkers = int(input("How many workers? "))
    while not (0 < numWorkers <= 100):
        print("Invalid input. The number of workers must be >0 snd <=100. Try again.")
        numWorkers = int(input("How many workers? "))
    return numWorkers

def getRate(workerNum):
    rate = float(input("\nEnter the hourly pay rate for worker " + str(workerNum) + ": "))
    while not (0 < rate <= 100):
        print("Invalid input. The number of workers must be >0 snd <=100. Try again.")
        rate = float(input("\nEnter the hourly pay rate for worker " + str(workerNum) + ": "))
    return rate

def getHours(workerNum2):
    hours = float(input("\nEnter the number of hours worked for worker " + str(workerNum2) + ": "))
    while not (0 < hours <= 100):
        print("Invalid input. The number of workers must be >0 snd <=100. Try again.")
        hours = float(input("\nEnter the number of hours worked for worker " + str(workerNum2) + ": "))
    return hours

def main():
    printInfo()
    totalPay = 0
    numWorkers = getNumWorkers()
    for worker in range(1,numWorkers+1):
        rate = getRate(worker)
        hours = getHours(worker)
        workerPay = calcPay(rate, hours)
        totalPay += workerPay
        print("This week's pay for worker " + str(worker) + " is: " + str(workerPay))
    print("Total weekly pay is: ", totalPay)

main()
