def printInfo():
    print("This program calculates the weekly pay for hourly workers.")
    print("Workers get \"time and a half\" for overtime.")
    print ("That is, for all hours worked above 40, they get paid at 1.5 times their regular hourly rate.")
    print ("Enter the number of workers for whom pay is to be calculated.")               
    print ("Then, for each worker, enter the hourly pay rate and the number of hours worked.\n")

def calcPay (rate, hours):
    if hours <=40:
        pay = round(rate*hours,2)
    else:
        pay = round(rate*40 + (hours-40)*rate*1.5,2)
    return pay

def main():
    printInfo()
    numWorkers = int(input("How many workers? "))
    for worker in range(1,numWorkers+1):
        rate = float(input("\nEnter the hourly pay rate for worker " + str(worker) + ": "))
        hours = float(input("Enter the number of hours worked for worker " + str(worker) + ": "))
        workerPay = calcPay(rate, hours)
        print("This week's pay for worker " + str(worker) + " is: $ " + str(workerPay))

main()
