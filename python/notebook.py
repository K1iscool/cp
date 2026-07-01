# Notebook program

# -------------------------
# Subprograms
# -------------------------
def get_note_number():
    valid_input = False
    while not valid_input:
        note_number = int(input("Note number: "))
        if note_number >= 0 and note_number < 10:
            valid_input = True
        else:
            print("Invalid input. Enter 0-9.")
    return note_number


def add_note():
    index = get_note_number()
    note = input("Enter the note: ")
    notebook[index] = note


def clear_notes():
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Are you sure you want to delete all notes? y/n :")
    if choice == "y":
        for index in range(len(notebook)):
            notebook[index] = ""


def order_notes():
    notebook.sort()


def show_notebook():
    for index in range(len(notebook)):
        print(index, ":", notebook[index])

def delete_notes():
    print("which note would you like to delete")
    index = get_note_number()
    notebook.pop(index)

def move_notes():
    print("which notes would you like to swap")
    index1 = get_note_number()
    index2 = get_note_number()
    thing = notebook[index1]
    notebook[index1] = notebook[index2]
    notebook[index2] = thing
    
def menu():
    print()
    print("a. Add note")
    print("d. Delete note")
    print("c. Clear notebook")
    print("m. Move note")
    print("o. Order notes")
    choice = input(":")
    
    match choice:
        case "a":
            add_note()
        case "d":
            delete_notes()
        case "c":
            clear_notes()
        case "m":
            move_notes()
        case "o":
            order_notes()
        
        
            
# -------------------------
# Main program
# -------------------------
notebook = ["" for note in range(10)]
while True:
    show_notebook()
    menu()