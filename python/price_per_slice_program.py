#price per slice program

#~~~~~~~~~~~~~~~~~~~
#sub
#~~~~~~~~~~~~~~~~~~~
    
def peopleS():
    people = int(input("how many people are eating "))
    if people == 1:
        print("you must pay the full bill duh")
    elif people == 2:
        person_a = int(input("how many slices did person A eat "))
        person_b = int(input("how many slices did person B eat "))
        person_a_price = person_a * slice_price
        person_b_price = person_b * slice_price
        print(f"person A must pay {person_a_price} and person B must pay {person_b_price}")
        
    elif people == 3:
        person_a = int(input("how many slices did person A eat "))
        person_b = int(input("how many slices did person B eat "))
        person_c = int(input("how many slices did person C eat "))
        person_a_price = person_a * slice_price
        person_b_price = person_b * slice_price
        person_c_price = person_c * slice_price
        print(f"person A must pay {person_a_price} ,person B must pay {person_b_price} and person C must pay {person_c_price}" )

    else:
        print("ERROR CODE: 936475")
    
    
    


#~~~~~~~~~~~~~~~~~~
#Main
#~~~~~~~~~~~~~~

print("welcome too the PPSP")

slices = int(input("how many slices are there "))
og_total = float(input("how much is the price in total "))
slice_price = og_total / slices
peopleS()

