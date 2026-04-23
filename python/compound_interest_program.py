# Compound interest program

# -------------------------
# Subprograms
# -------------------------
def compound(balance, interest_rate, target_balance, year):
  if balance <= target_balance:
    year = year + 1
    balance = balance + balance * interest_rate
    print("Year", year,": Balance £", balance)
    return compound(balance, interest_rate, target_balance ,year)
    
    

# -------------------------
# Main program
# -------------------------
year = 1
print("welcome to the intrest calculator")
balance = int(input("enter the balance to the nearest pound: "))
interest_rate = int(input("enter the % intrest rate: ")) / 100
target_balance = int(input("enter the target balance to the nearest pound: "))


compound(balance, interest_rate, target_balance ,year)
