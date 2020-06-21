def main():
    coded = input("Enter the coded message: ")
    lstCode = [int(i) for i in coded.split()]
    lst1 = []
    for i in lstCode:
        i = str(chr(i))
        lst1.extend(i)
    str1 = ''.join(lst1)
    print("The decoded message is:",str1)

main()
