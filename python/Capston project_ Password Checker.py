#====================================
# CAPSTONE PROJECT: PASSWORD CHECKER
#====================================

#======================
# PASSWORD SUB-PROGRAM
#======================

def check_password():
    attempt = 0
    while attempt < 3:
        attempt = attempt + 1
        if (input("Enter Password: ")) == "LetMeIn":
            print("Login Successful")
            break
        elif attempt == 3:
            print("Max Attempts Reached")
        else:
            print("Incorrect Password")
#===========
# main
#===========

print(''''Welcome
Please input your password''')
check_password()