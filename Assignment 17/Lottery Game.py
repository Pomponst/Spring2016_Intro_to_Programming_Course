import random

winnings = 0

numSpin = int(input("Please enter the number of games you wish to play? "))
print()
for i in range(0,numSpin):
    guess = int(input("Enter your guess. "))
    while guess < 1 or guess > 99:
        print("Invalid guess")
        guess = int(input("Enter your guess. "))
    spin = random.randint(1,99)
    print("The wheel landed on",spin)
    if guess == spin:
        if 50 * guess > 2500:
            won = 50 * guess
        else:
            won = 2500
        print("You win $"+str(won)+"\n")
        winnings += won
    elif abs(guess - spin)<25:
        reroll = input("Do you wish to spin the wheel for your prize (y/n)? ")
        reroll = reroll.lower()
        while reroll not in ("y","yes","n","no"):
            print("Invalid entry")
            reroll = input("Do you wish to spin the wheel for your prize (y/n)? ")
            reroll = reroll.lower()
        if reroll == "y":
            spin = random.randint(1,99)
            print("The wheel landed on",spin)
            print("You win $"+str(spin*20)+"\n")
            winnings += (spin*20)
        elif reroll == "n":
            print("You win $750\n")
            winnings += 750
    else:
        print("You lose.\n")

print("Your total for",str(numSpin),"games is $"+str(winnings)+".")
