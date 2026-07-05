import sys 
import numberconv

def showMenu():
    print("=== Welcome to the converter menu! ===")
    print("1) Dezimal to Binary")
    print("2) Binary to Decimal")
    print("3) Decimal to Hexadecimal")
    print("4) exit \n")

    selection = input("Please choose an option(1-3): ")

    if selection == "1":
        number = input("Please enter the decimal number: ")
        print(numberconv.decToBin(number))
    elif selection == "2":
        number = input("Please enter the binary number: ")
        print(numberconv.binToDec(number))
    elif selection == "3":
        number = input("Please enter the decimal number: ")
        print(numberconv.decToHex(number))
    elif selection == "3": 
        print("Converter closed")
        sys.exit()
    else:
        print("Invalid selection.")