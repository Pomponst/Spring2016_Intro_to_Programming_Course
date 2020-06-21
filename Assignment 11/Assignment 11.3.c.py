##Variables
pmt = float(input("Starting balance: "))
beg = int(input("Starting interest rate: "))
end = int(input("Ending interest rate: "))
time = int(input("Number of years: "))
lst1 = range(beg,end+1,1)
counter = 1

##Logic
for i in lst1:
    print("Interest rate of "+str(i)+" %:")       
    while counter <= time:
        pmt = pmt + (pmt * (i/100))
        print("Balance after year "+str(counter)+" is $ "+str(round(pmt,2)))
        counter += 1
    counter = 1
    pmt = 1000
    print("\n")
