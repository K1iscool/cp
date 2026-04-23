#=============
# PIN PROGRAM
#=============

#=============
# MAIN
#=============
attempt = 0
while attempt < 3:
    attempt = attempt + 1
    if int(input("Enter PIN: ")) == 2077:
        print("access granted")
        break
    elif attempt == 3:
        print("access denied")