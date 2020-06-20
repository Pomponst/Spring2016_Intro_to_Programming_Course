##Input
start = float(input("Enter the starting value: "))
end = float(input("Enter the ending value: "))
incr = float(input("Enter the increment: "))
print("\n")

##Heading
print("Gallons","\t","Liters")

##Logic
while start <= end:
    print(start,"\t\t",round((start*3.785),2))
    start = start + incr
