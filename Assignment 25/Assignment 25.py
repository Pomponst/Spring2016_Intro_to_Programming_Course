def main():
    listVP = createListFromFile("VPres.txt")
    createFileWithCommonItems(listVP, "USPres.txt", "Both.txt")

def createListFromFile(inFileName):
    infile = open(inFileName, 'r')
    lst = []
    for line in infile:
        lst.append(line)
    infile.close()
    return lst

def createFileWithCommonItems(lst, inFileName, outFileName):
    infile = open(inFileName, 'r')
    outfile = open(outFileName, 'w')
    for item in infile:
        if item in lst:
            outfile.write(item)
    infile.close()
    outfile.close()

main()
