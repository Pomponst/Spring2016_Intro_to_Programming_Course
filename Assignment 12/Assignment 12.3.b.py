def maxFun (val1, val2, val3):
    max = val1
    if val2 > max:
        max = val2
    if val3 > max:
        max = val3
    print ("The maximum is: ",max)

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    maxFun(number1,number2,number3)

main()
