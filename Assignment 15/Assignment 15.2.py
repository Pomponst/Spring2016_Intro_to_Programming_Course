def choice():
    print("Enter 1 to encode a character string into Unicode")
    print("Enter 2 to decode a Unicode string into characters")
    choice = int(input("Choice: "))
    while choice not in [1,2]:
        print("Invalid choice. Please try again.")
        print("Enter 1 to encode a character string into Unicode")
        print("Enter 2 to decode a Unicode string into characters")
        choice = int(input("Choice: "))
    return choice

def encode():
    coded = input("Enter the character string to encode: ")
    lst1 = []
    for i in coded:
        i = ord(i)
        lst1.append(i)
    str1 = ' '.join(str(e) for e in lst1)
    print("The encoded message is:",str1)

def decode():
    coded = input("Enter the Unicode string to decode: ")
    lstCode = [int(i) for i in coded.split()]
    lst1 = []
    for i in lstCode:
        i = str(chr(i))
        lst1.extend(i)
    str1 = ''.join(lst1)
    print("The decoded message is:",str1)


def main():
    x = choice()
    if x == 1:
        encode()
    if x == 2:
        decode()

main()
