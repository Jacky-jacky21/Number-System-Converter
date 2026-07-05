import argparse
import numberconv
import menu

def main():
    parser = argparse.ArgumentParser(description="Simple Number-Converter.")
    parser.add_argument("--dectobin", metavar="<DECIMAL NUMBER>", help="Convert immediately, Decimal to Binary", type=str)
    parser.add_argument("--bintodec", metavar="<BINARY NUMBER>", help="Convert immediately, Binary to Decimal", type=str)
    #TODO: add all short forms for the new number systems
    args = parser.parse_args()

    #Convert immediately
    #dtb
    if args.dectobin:
        result = numberconv.decToBin(args.dectobin)
        print(result)
        
    #btd
    if args.bintodec:
        result = numberconv.binToDec(args.bintodec)
        print(result)

    #Open menu
    else:
        menu.showMenu()

if __name__ == "__main__":
    main()