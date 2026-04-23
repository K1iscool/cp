# Denary to binary program

#=========#
# IMPORTS #
#=========#

import math

#========#
# BINARY #
#========#

def den_to_bin(number):

    binary = ""

    while number > 0:

        remainder = number % 2

        binary = str(remainder) + binary

        number = number // 2

    return binary

#=======#
# OCTAL #
#=======#

def den_to_oct(number):
    octal = oct(number)
    return octal

#=============#
# HEXADECIMAL #
#=============#

def den_to_hex(number):
    hexa = str(hex(number))
    hexa = hexa[2:].upper()
    return hexa

#======#
# MAIN #
#======#

number = int(input("Enter the denary number to convert: "))

print("Binary:", den_to_bin(number))
print(f"Octal: {den_to_oct(number)[2:]}")
print(f"Hexadecimal: {den_to_hex(number)}")

