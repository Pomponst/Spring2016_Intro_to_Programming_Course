state = input("Enter the two character abbreviation for the state: ")
state = state.upper()
listUniv = []
univCount = []
foundFlag = False
infile = open("UniversitiesWithStates.txt", 'r')
for line in infile:
    listUniv.append(line[-3:])
infile.close()
for line in listUniv:
    line = line.rstrip()
    if line == state:
        univCount.append(state)
        foundFlag = True
if foundFlag == True:
    print("The number of unversities in",state,"is "+str(len(univCount)))
if not foundFlag:    
    print("There are no universities listed in "+state+". Check your spelling.")
