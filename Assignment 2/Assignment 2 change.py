price = int(input("How much does the item cost (in cents)?"))
change = 100 - price
## print("You should get",change,"cents back.")
q = change // 25
change = change % 25
## print("Change after quarters =", change)
d = change // 10
change = change % 10
## print("Change after dimes =", change)
n = change // 5
change = change % 5
## print("Change after nickles =", change)
p = change

print("Your change is",q,"quarter(s)",d,"dime(s)",n,"nickle(s)",p,"penny/pennies")
