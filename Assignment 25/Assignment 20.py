infile = open("USPres.txt", 'r')
listPres = []
for line in infile:
    listPres.append(line.rstrip())
infile.close()

infile = open("VPres.txt", 'r')
listVPs = []
for line in infile:
    listVPs.append(line.rstrip())
infile.close()
        
listBoth = []
for pres in listPres:
    if pres in listVPs:
        listBoth.append(pres + '\n')

outfile = open("Both.txt", 'w')
outfile.writelines(listBoth)
outfile.close()
