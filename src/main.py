import argparse
import numberconv
import menu

__version__ = "1.0.0"

def main():
    parser = argparse.ArgumentParser(
        description=(
            "=== Simple Number-Converter ===\n"
            "A powerful CLI tool to convert numbers between different systems.\n"
            "If no flags are provided, the interactive menu will open automatically. \n"
        ), 
    epilog=(
            "Examples:\n"
            "  python main.py --dectobin 42\n"
            "  python main.py -dh 255\n\n"
            f"Version: {__version__} | Created by Jacky-jacky21 (2026)."
        ),
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-db", "--dectobin", metavar="<DEC>", help="Convert Decimal to Binary", type=str)
    parser.add_argument("-dh", "--dectohex", metavar="<DEC>", help="Convert Decimal to Hexadecimal", type=str)
    parser.add_argument("-bd", "--bintodec", metavar="<BIN>", help="Convert Binary to Decimal", type=str)
    parser.add_argument("-bh", "--bintohex", metavar="<BIN>", help="Convert Binary to Hexadecimal", type=str)
    parser.add_argument("-hd", "--hextodec", metavar="<HEX>", help="Convert Hexadecimal to Decimal", type=str)
    parser.add_argument("-hb", "--hextobin", metavar="<HEX>", help="Convert Hexadecimal to Binary", type=str)
    parser.add_argument("-v", "--version", action="version", version=f"Number-Converter v{__version__}")
    args = parser.parse_args()

    #Convert immediately
    #dtb
    if args.dectobin:
        result = numberconv.decToBin(args.dectobin)
        print(result)

    #dth
    elif args.dectohex:
        result = numberconv.decToHex(args.dectohex)
        print(result)
        
    #btd
    elif args.bintodec:
        result = numberconv.binToDec(args.bintodec)
        print(result)

    #bth
    elif args.bintohex:
        result = numberconv.binToHex(args.bintohex)
        print(result)

    #htd
    elif args.hextodec:
        result = numberconv.hexToDec(args.hextodec)
        print(result)

    #htb
    elif args.hextobin:
        result = numberconv.hexToBin(args.hextobin)
        print(result)

    #Open menu
    else:
        print("=== Welcome to the converter menu! ===")
        while True:
            menu.showMenu()

if __name__ == "__main__":
    main()