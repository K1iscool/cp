#==================================#
# MASTERING: ADVANCED LOGIN SYSTEM #
#==================================#

#=========#
# IMPORTS #
#=========#

import sys

#==============================#
# USERNAME CREATING SUBPROGRAM #
#==============================#

def namesub():
    global username
    username = input("Please input your new username")
    usercheck = False
    while usercheck == False:
        if len(username) > 4 and len(username) < 16 and ' ' not in username:
            usercheck = True
            passsub()
        else:
            print("Username must be between 5 and 15 characters and have no spaces")
            namesub()
#==============================#
# PASSWORD CREATING SUBPROGRAM #
#==============================#

def passsub():
    global password
    password = input("Please input your new password")
    passcheck = False
    while passcheck == False:
        if len(password) > 7 and any(char.isupper()for char in password) and any(char.isdigit() for char in password):
            print("New user created!")
            menu()
        else:
            print("Password must be longer than 8 characters and have ateast one number")
            passsub()

#==================#
# LOGIN SUBPROGRAM #
#==================#

def login():
    login_atempts = 0
    while login_atempts < 3:
        user_atempt = input("Please enter your user name")
        pass_atempt = input("Please enter your password")
        if pass_atempt == password and user_atempt == username:
            print(f"Welcome {username}")
            break
        else:
            login_atempts = login_atempts + 1
            print(f"Attempt {login_atempts} of 3")

#=================#
# MENU SUBPROGRAM #
#=================#

def menu():
    menu_option = 0
    print("Welcome to the login manager please select an option")
    try:
        menu_option = int(input('''
1) Create new user
2) Use existing user
3) Exit
 '''))
        if menu_option == 1:
            namesub()
        elif menu_option == 2:
            login()
        elif menu_option == 3:
           sys.exit()
        else:
            print("Invalid option")
            menu()
    except ValueError:
        menu()
#======#
# MAIN #
#======#

menu()
