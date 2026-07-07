import argparse
import sys

ERRMSG = "Error: wrong input!"
#Decimal stuff
#Decimal to binary
def decToBin(number):
    try:
        return bin(int(number)).replace("0b", "")
    except ValueError:
        return ERRMSG
    
#Decimal to Hexadecimal   
def decToHex(number):
    try: 
        return hex(int(number)).replace("0x", "").upper()
    except ValueError:
        return ERRMSG
    

#Binary stuff
#Binary to Decimal
def binToDec(number):
    try:
        return str(int(number, 2))
    except ValueError:
        return ERRMSG
    
#Binary to Hexadecimal
def binToHex(number):
    try:
        return hex(int(number, 2)).replace("0x", "").upper()
    except ValueError:
        return ERRMSG

#Hexadecimal stuff   
#Hexadecimal to Decimal
def hexToDec(number):
    try:
        return str(int(number, 16))
    except ValueError:
        return ERRMSG
    
#Hexadecimal to Binary
def hexToBin(number):
    try:
        return bin(int(number, 16)).replace("0b", "")
    except ValueError:
        return ERRMSG
        
