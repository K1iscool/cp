#========================#
# GUNGEON MASTER PROGRAM #
#========================#

#=========#
# IMPORTS #
#=========#

from random import randint

#=============#
# SKILL CHECK #
#=============#

def skill_check():
    usr_roll = randint(1, 20)
    print(f"You rolled a {usr_roll}")
    roll_x_mod_x_skill = usr_roll + skill_val + mods
    if usr_roll == 1:
        print("Critical Fail")
    elif usr_roll == 20:
        print("Critical Success")
    elif roll_x_mod_x_skill >= num_to_pass:
        print("Check Passed")
    elif roll_x_mod_x_skill < num_to_pass:
        print("Check Failed")

#======#
# main #
#======#

skill_val = int(input("Enter the skill value: "))
mods = int(input("Enter any modifiers: "))
num_to_pass = int(input("Enter the number to pass: "))
auto_pass = num_to_pass + 5
if skill_val + mods >= auto_pass:
    print("Automatic Pass")
else:
    skill_check()
