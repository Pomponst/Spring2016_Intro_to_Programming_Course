str1 = input("Please enter a string:")

if str1.isalpha():
    if str1.islower():
        print("Your string is comprised entirely of lower case letter.")
    else:
        print("Your string is comprised entirely of letters but some or all are upper case.")
else:
    print("Your string is not comprised entirely of letters.")
