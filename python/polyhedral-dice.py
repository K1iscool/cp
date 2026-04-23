#=========================#
# POLYHEDRAL DICE PROGRAM #
#=========================#

#=========#
# IMPORTS #
#=========#

import random

#=============#
# sub program #
#=============#

def roll_dice():
    if dice_choice == 6:
        return random.randint(1, 6)
    elif dice_choice == 8:
        return random.randint(1, 8)
    elif dice_choice == 10:
        return random.randint(1, 10)
    elif dice_choice == 12:
        return random.randint(1, 12)
    else:
        print("Please input a valid number D(6, 8, 10, 12)")
        
#======#
# main #
#======#

dice_choice = int(input("Roll a D"))
random.seed()
number = roll_dice()
if number == 8 or number == 11:
    print(f"You rolled an {number}")
else:
    print(f"You rolled a {number}")
