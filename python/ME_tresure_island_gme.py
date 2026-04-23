# ----------------
# Constants
# ----------------

from time import sleep

#ascii_art = '''
#                            _.--.
#                        _.-'_:-'||
#                    _.-'_.-::::'||
#               _.-:'_.-::::::'  ||
#             .'`-.-:::::::'     ||
#            /.'`;|:::::::'      ||_
#           ||   ||::::::'     _.;._'-._
#           ||   ||:::::'  _.-!oo @.!-._'-.
#          \'.  ||:::::.-!()oo @!()@.-'_.
#            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
#              `>'-.!@%()@'@_%-'_.-o _.|'||
#               ||-._'-.@.-'_.-' _.-o  |'||
#               ||=[ '-._.-\U/.-'    o |'||
#               || '-.]=|| |'|      o  |'||
#               ||      || |'|        _| ';
#               ||      || |'|    _.-'_.-'
#               |'-._   || |'|_.-'_.-'
#                '-._'-.|| |' `_.-'
#                    '-.||_/.-'
#'''

# ----------------
# Subprograms
# ----------------

def game():
    swim_or_wait = input("You come to a lake. Do you either want to wait for a boat, or swim across? (swim/wait): ")
    if swim_or_wait == "swim":
        print("You got eaten by a hungry shark. Game over.")
    elif swim_or_wait == "wait":
        print("A boat arrives and you use it to get to the island safley")
        cave_or_stay = input("You come to a cave, do you want to venture inside or walk on? (venture/walk):")
        if cave_or_stay == "venture":
            print("You are squished by boulders never to be seen again. Game over")
        elif cave_or_stay == "walk":
            print("You walk away from the cave along a narrow track in the forest")
            crossroad_turn = input("You eventually reach a crossroad. Do you go left, right or straight? (left/right/straight): ")
            if crossroad_turn == "left":
                print("You are trampled by a herd of wilderbeast. Game over")
            elif crossroad_turn == "straight":
                print("You get stung by a poisonous wasp. Game over")
            elif crossroad_turn == "right":
                print("You march on and rind the tresure, wahoo!")
               # print(ascii_art)
# ----------------
# Main program
# ----------------

print("Welcome to Tresure Island a choose-your-own-adventure game.")
sleep(5)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Legend has it that there is some buried treasure on the island you are exploring... So you have decided to go in search of it.")
game()




















