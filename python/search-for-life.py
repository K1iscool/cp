# Search for life program



# -------------------------

# Import libraries

# -------------------------

import random





# -------------------------

# Subprograms

# -------------------------

def probe(planet):    

    creature = ["lizards", "humanoids", "insects"]

    colour = ["red", "green", "blue"]

    characteristic = ["shy", "angry", "docile"]
    
    temp = ["barren", "hot", "cold", "temperate"]
    

    random.seed(planet)

    lifeform = random.randint(0,2)

    specimen = random.randint(0,2)

    behaviour = random.randint(0,2)

    planet = random.randint(0,3)



    report = ""

    

    report = colour[specimen]

    report = report + ", " + characteristic[behaviour]

    report = report + " " + creature[lifeform]

    report = report + " on a " + temp[planet] + " planet"

    if "temperate" in report:
        return report
    else:
        return f"a {temp[planet]} planet with no sighns of life"
    

    

# -------------------------

# Main program

# -------------------------

planet = int(input("Enter the catalogue number of a planet: "))

report = probe(planet)

print("Probes report", report)


