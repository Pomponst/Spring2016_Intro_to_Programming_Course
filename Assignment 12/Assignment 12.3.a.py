def findAbs (value):
    if value >=0:
        return value
    else:
        return -value

def main():
    number = float(input("Enter a number: "))
    absVal = findAbs(number)
    print("The absolute value of",number,"is:",absVal)

main()
