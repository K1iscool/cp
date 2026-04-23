# Leap year program

#=====#
# Sub #
#=====#
def is_leap_year(year):
    year_divided = year / 400
    if int(year_divided) == year_divided:
        return True
    else:
        year_divided = year / 100
        if int(year_divided) == year_divided:
            return False
        else:
            year_divided = year / 4
            if int(year_divided) == year_divided:
                 return True
    return False

#==============#
# Main program #
#==============#
year =int(input("Please input a year"))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(f"{year} is not a leap year")

