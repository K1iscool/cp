#=============#
# RPS PROGRAM #
#=============#

#=========#
# IMPORTS #
#=========#

from random import randint

#===============#
# PLAYER CHOICE #
#===============#

def get_player_choice():
    pc = input("Enter rock, paper or scissors (r,p,s): ")
    return pc
#============#
# CPU CHOICE #
#============#

def cpu_choice():
    cc = randint(1,3)
    if cc == 1:
        cc = "r"
    elif cc == 2:
        cc = "p"
    else:
        cc = "s"
    return cc

#===============#
# WHO WON ROUND #
#===============#

def who_won_round(pc, cc):
    # PLAYER WIN #
    if pc == "r" and cc == "s":
        return "the player wins"
    elif pc == "p" and cc == "r":
        return "the player wins"
    elif pc == "s" and cc == "p":
        return "the player wins"
    # CPU WIN #
    elif cc == "r" and pc == "s":
        return "the CPU wins"
    elif cc == "p" and pc == "r":
        return "the CPU wins"
    elif cc == "s" and pc == "p":
        return "the CPU wins"
    # DRAW #
    else:
        return "a draw"

#===========#
# PLAY GAME #
#===========#

def play_game(player_win_count, cpu_win_count):
    while player_win_count < 10 and cpu_win_count < 10:
        pc = get_player_choice()
        cc = cpu_choice()
        winner = who_won_round(pc, cc)
        if winner == "the player wins":
            player_win_count = player_win_count + 1
        elif winner == "the CPU wins":
            cpu_win_count = cpu_win_count + 1 
        print(f"player score: {player_win_count} cpu_score {cpu_win_count}")
        print(f"The result is {winner}")
    if player_win_count == 10:
        print("PLAYER WINS!")
    else:
        print("CPU WINS!")
     

#======#
# main #
#======#
player_win_count = 0
cpu_win_count = 0
play_game(player_win_count, cpu_win_count)

