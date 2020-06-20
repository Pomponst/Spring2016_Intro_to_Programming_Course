print("s-for single")
print("m-for married")
print("d-for divorced")
print("w-for widowed")

##Input
marital = str(input("What is your marital status?"))

##Logic
if marital == "s":
    print("You are single.")
elif marital == "m":
    print("You are married.")
elif marital == "d":
    print("You are divorced.")
elif marital == "w":
    print("You are widowed.")
else:
    print("You have entered an unrecognizable marital status.")
