#=============#
# LCM PROGRAM #
#=============#

#=====#
# sub #
#=====#

def lmc(number_one, number_two):
    if number_one > number_two:
        counter = number_one
    else:
        counter = number_two
    while counter % number_one != 0 or counter % number_two != 0:
        counter = counter + 1
    return counter

#======#
# main #
#======#

number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))
result = lmc(number_one, number_two)
print(f"The LMC of {number_one} and {number_two} is {result}")

