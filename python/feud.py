#==============#
# Feud program␍#
#==============#


# -------------------------
# Subprograms
# -------------------------
def forage_herb(herbs, spells):
    choice = input("What herb would you like to look for?: ")
    choice = choice.lower()
    herbs_checklist = ["dandelion", "burdock", "pipewort", "ragwort", "snapdragon", "toadflex"]
    if choice in herbs_checklist:
        herbs.append(choice)
    else:
        print(f"Couldnt Find {choice}")

def cauldron(herbs, spell):
    choice = input("What spell do you want to brew: ")
    choice = choice.lower()
    if choice == "teloport" and "dandelion" in herbs and "burdock" in herbs:
        spells.append(choice)
        herbs.remove("dandelion")
        herbs.remove("burdock")
        print(f"{choice} brewed")
    
    elif choice == "protect" and "pipewort" in herbs and "ragwort" in herbs:
        spells.append(choice)
        herbs.remove("pipewort")
        herbs.remove("ragwort")
        print(f"{choice} brewed")
    elif choice == "sprites" and "snapdragon" in herbs and "toadflex" in herbs:
        spells.append(choice)
        herbs.remove("snapdragon")
        herbs.remove("toadflex")
        print(f"{choice} brewed")
    else:
        print("Spell failed")


def brew_spell():
    gay = False


       
def cast_spell(spells):
    choice = input("What would you like to cast: ")
    if choice in spells:
        spells.remove(choice)
        print(f"{choice} has been cast")
    else:
        print("You have not brewed that spell")


def take_action(herbs, spells):
    choice = input("Forage herb, brew or cast a spell F/B/C: ")
    choice = choice.upper()
    if choice == "F":
        forage_herb(herbs, spells)
    elif choice == "B":
        cauldron(herbs, spells)
    elif choice == "C":
        cast_spell(spells)

# -------------------------␍
# Main program␍
# -------------------------␍
herbs = []
spells = []
gay = True
while gay:
    take_action(herbs, spells)
