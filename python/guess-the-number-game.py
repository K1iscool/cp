#=======================#
# GUESS THE NUMBER GAME #
#=======================#

#=========#
# IMPORTS #
#=========#

from random import randint

#=====#
# sub #
#=====#

def game_logic(lowest, highest, guess_counter):
    number = randint(lowest, highest)
    game_won = False
    while game_won == False:
        guess = int(input("Enter the number im thinking of? "))
        guess_counter = guess_counter + 1
        if guess == number:
            game_won = True
            print(f"You've got it, I chose {number} It took you {guess_counter} guesses.")

#======#
# main #
#======#

lowest = int(input("What is the lowest number I can chose? "))
highest = int(input("What is the highest number I can chose? "))
print("Ok, lets play. I wonder how many guesses it will take you.")
guess_counter = 0
game_logic(lowest, highest, guess_counter)
