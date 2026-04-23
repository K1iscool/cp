#=======================#
# RANDOM NAME GENERATOR #
#=======================#

#=========#
# IMPORTS #
#=========#

import random

#=====#
# sub #
#=====#

def generate_name():
    forename = ["Muhammad","Noah","Jack","Lily","Sophia","Olivia"]
    surname = ["Wang","Smith","Devi","Jones","Kim","Rodriguez"]
    fn_number = random.randint(0,5)
    sn_number = random.randint(0,5)
    return f"{forename[fn_number]} {surname[sn_number]}"

#======#
# main #
#======#

print(generate_name())

