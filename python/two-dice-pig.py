#Two-dice pig program



# -------------------------

# Import libraries

# -------------------------

import random





# -------------------------

# Subprograms

# -------------------------

def roll():

    dice = [0, 0]

    dice[0] = random.randint(1, 6)

    dice[1] = random.randint(1, 6)

    return dice    





def points(dice):

    if dice[0] == 1 and dice[1] == 1:

        return -1

    elif dice[0] == 1 or dice[1] == 1:

        return 0

    else:

        return dice[0] + dice[1]





def play_game():
    player_count = int(input("How many players? 1-4: "))

    random.seed()

    score = [0, 0, 0, 0]

    player = 0

    new_player = True
    
    winner = -1

    while winner == -1:

        if new_player:

            print()

            print("------------------------------------")

            print("Player", player + 1, "it's your turn.")

            print("Your score is currently:", score[player])

            total = 0 

            new_player = False

            turn_end = False

        print("Press Enter to roll the dice.")

        input()

        dice = roll()

        result = points(dice)

        print("You rolled a", dice[0], "and", dice[1])

        if result > 0:

            print("You scored", result)

            total = total + result

            print("Your total is", total)

            choice = ""

            while choice not in ["y", "n"]:

                choice = input("Do you want to continue y/n? :")

            if choice == "n":

                score[player] = score[player] + total
                
                if score[player] >= 100:
                    winner = player
                else:
                    turn_end = True
                if winner != -1:
                    print(f"Player {player + 1} wins!")
        elif result == -1:
            print("Oh no, that's a double pig out, back to zero")

            total = 0

            turn_end = True
        else:

            print("Oh no, that's a pig out!")

            turn_end = True

        if turn_end:

            print("Press Enter to hand the dice to the next player.")

            input()

            player = (player + 1) % player_count

            new_player = True





# -------------------------

# Main program

# -------------------------

play_game()
