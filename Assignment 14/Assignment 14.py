import random

def printInfo():
    print("See if you can predict if the computer flips heads or tails.")
    number = int(input("Number of times to flip coin: "))
    while number <= 0:
        print(number,"Is not a valid entry. Please enter any number greater than 0")
        number = int(input("Number of times to flip coin: "))
    return number

def coinToss(number):
    for amount in range(number):
         flip = random.randint(0, 1)
         if (flip == 0):
             guess = int(input("\nEnter your guess. 0 for tails or 1 for heads: "))
             while guess not in [0,1]:
                 print(guess,"Is not a valid entry. Please try again.")
                 guess = int(input("Enter your guess. 0 for tails or 1 for heads: "))
             print("The flip is tails.")
             if guess == 0:
                 print("Correct guess.")
                 correctList.append(1)
             else:
                 print("Sorry. That's not correct.")
         else:
             guess = int(input("\nEnter your guess. 0 for tails or 1 for heads: "))
             while guess not in [0,1]:
                 print(guess,"Is not a valid entry. Please try again.")
                 guess = int(input("Enter your guess. 0 for tails or 1 for heads: "))
             print("The flip is heads.")
             if guess == 1:
                 print("Correct guess.")
                 correctList.append(1)
             else:
                 print("Sorry. That's not correct.")
                 
def summary():
    print("\nThe coins was flipped",number,"times.")
    print("You guessed correctly",len(correctList),"time(s).")
    print("Your percentage correct is:",round((len(correctList)/number)*100,2),"%.")

def main():
    printInfo()
    correctList = []
    heads = 0
    tails = 0
    coinToss()
    summary()

main()
