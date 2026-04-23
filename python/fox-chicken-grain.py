#==================================#
# FOX CHICKEN GRAIN PUZZLE PROGRAM #
#==================================#

#========#
# OUTPUT #
#========#

def output():
    print('''-----------------------
This side of the river:''')
    if fox == 0:
        print("Fox")
    if chicken == 0:
        print("Chicken")
    if grain == 0:
        print("Grain")
    if farmer == 0:
        print("Farmer")
    print(" ")
    print("The other side of the river")
    if fox == 1:
        print("Fox")
    if chicken == 1:
        print("Chicken")
    if grain == 1:
        print("Grain")
    if farmer == 1:
        print("Farmer")
    print("-----------------------")

#=============#
# WRONG MOVES #
#=============#

def wrong_move(game_failed):
    if farmer != fox and fox == chicken:
        print("The fox ate the chicken")
        game_failed = True
        return game_failed
    elif farmer != chicken and chicken == grain:
        print("The chicken ate the grain")
        game_failed = True
        return game_failed
    else:
        game_failed = False
        return game_failed

#================#
# GAME WON CHECK #
#================#

def game_won_check(game_won):
    if fox == 1 and farmer == 1 and chicken == 1 and grain == 1:
        game_won = True
        return game_won
    else:
        game_won = False
        return game_won

#======#
# MAIN #
#======#
game_won = False
game_failed = False
choice = ""
fox = 0
chicken = 0
grain = 0
farmer = 0
print("") # add opening text here #
while game_won == False and game_failed == False:
    choice = input("Which item do you take in your rowboat: ")
    if choice == "fox":
        fox = 1
        farmer = 1
    elif choice == "chicken":
        chicken = 1
        farmer = 1
    elif choice == "grain":
        grain = 1
        farmer = 1
    elif choice == "farmer":
        farmer = 1
    output()
    game_failed = wrong_move(game_failed)
    game_won = game_won_check(game_won)
    if game_won or game_failed:
        break
    return_choice = input("Which item do you take back in your rowboat: ")
    if return_choice == "fox":
        fox = 0
        farmer = 0
    elif return_choice == "chicken":
        chicken = 0
        farmer = 0
    elif return_choice == "grain":
        grain = 0
        farmer = 0
    elif return_choice == "farmer":
        farmer = 0
    output()
    game_failed = wrong_move(game_failed)
    game_won = game_won_check(game_won)

if game_won == True:
    print("You solved the puzzle.")

else:
    print("")
