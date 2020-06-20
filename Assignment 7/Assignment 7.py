##Input
letter = input(str("Enter a letter:"))
letter = letter.upper()

##Logic
if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print(letter,"is a vowel.")
elif letter.isalpha():
    print(letter,"is not a vowel")
else:
    print("You did not enter a letter.")
