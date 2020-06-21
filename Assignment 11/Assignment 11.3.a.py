##Variables
pmt = 1000
per = .06
time = 5
counter = 1

##Logic
for i in [.03,.04,.05]:
    print("Interest rate of "+str(i*100)+" %:")
    for i in [.03,.05,.01]:
        pmt = pmt + (pmt * i)
        print(pmt)
        print("Balance after year "+str(counter)+" is $ "+str(round(pmt,2)))
        counter += 1
    counter = 1
    print("\n")
