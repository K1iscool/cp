#==========#
# CUP DRAW #
#==========#

# -------------------------
# Import libraries
# -------------------------

import random as r

# -------------------------
# Subprograms
# -------------------------

def input_teams(teams):
    gay = True
    while gay:
        teams.append(input("Enter the new team: "))
        teams.append(input("Enter the new team: "))
        gaychk = input("Would you like to add another set teams (Y/N)")
        gaychk = gaychk.upper()
        if gaychk == "Y":
            gay = gay
        else:
            gay = False
            return gay





def draw_teams(teams):
    r.shuffle(teams)
    print("""

The draw is
          """)
    while len(teams) > 0:
        teams_extract = teams.pop()
        teams_extract2 = teams.pop()
        if teams_extract == "bye":
            print(f"{teams_extract2} has no competition")
        elif teams_extract2 == "bye":
            print(f"{teams_extract} has no competition")
        else:
            print(f"{teams_extract} v {teams_extract2}")


        

        

# -------------------------
# Main program
# -------------------------

teams = []

input_teams(teams)

draw_teams(teams)


