import sys 
import numberconv


CONVERTER_MAP = {
    ("Decimal", "Binary"): numberconv.decToBin,
    ("Decimal", "Hexadecimal"): numberconv.decToHex,
    ("Binary", "Decimal"): numberconv.binToDec,
    ("Binary", "Hexadecimal"): numberconv.binToHex,
    ("Hexadecimal", "Decimal"): numberconv.hexToDec,
    ("Hexadecimal", "Binary"): numberconv.hexToBin,
    #If both are the same
    ("Decimal", "Decimal"): lambda x: x,
    ("Binary", "Binary"): lambda x: x,
    ("Hexadecimal", "Hexadecimal"): lambda x: x,
}

SYSTEM_NAMES = {
    "1": "Decimal",
    "2": "Binary",
    "3": "Hexadecimal",
}


def showMenu():
    #Source
    print("\nSelect the SOURCE system:")
    print("1) Decimal")
    print("2) Binary")
    print("3) Hexadecimal")
    print("4) Exit program")
    sourceSelection = input("Please choose an option (1-4): ").strip()

    if sourceSelection == "4":
        print("Converter closed.")
        sys.exit()
        
    if sourceSelection not in SYSTEM_NAMES:
        print("Invalid selection.")
        return
    
    #Target
    print("\nSelect the TARGET system:")
    print("1) Decimal")
    print("2) Binary")
    print("3) Hexadecimal")
    print("4) Return")
    targetSelection = input("Please choose an option (1-4): ").strip()

    if targetSelection == "4":
        print("\nBack to the source menu...")
        return

    if targetSelection not in SYSTEM_NAMES:
        print("Invalid selection.")
        return
    
    sourceSystem = SYSTEM_NAMES[sourceSelection]
    targetSystem = SYSTEM_NAMES[targetSelection]

    number = input(f"\nPlease enter the {sourceSystem} number: ")
    
    search = (sourceSystem, targetSystem)
    
    if search in CONVERTER_MAP:
        convertFunktion = CONVERTER_MAP[search]
        
        result = convertFunktion(number)
        print(f"\nConversion from {sourceSystem} to {targetSystem}")
        print(f"\nResult ({targetSystem}): {result}")
    else:
        print(f"\n[Error] Conversion from {sourceSystem} to {targetSystem} is not supported yet!")
