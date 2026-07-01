# Times tables program

# -------------------------
# Subprograms
# -------------------------
# Procedure to output the X times table.
def times_table(x):
    i = 1
    for i in range(1, 13):
        if i < 13:
            print(f"{i} x {x} = {i*x}")
        else:
            break
# -------------------------
# Main program
# -------------------------
x = int(input("which times table would you like: "))
times_table(x)
