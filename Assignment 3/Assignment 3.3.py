name = str(input("Please enter your full name:"))
space = name.find(" ")
fname = name[:space]
lname = name[space+1:]
print("Your first name is:",fname)
print("Your last name is:",lname)
