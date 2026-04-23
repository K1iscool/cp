# Seconds in a day program

#=======#
# HOURS #
#=======#
def seconds_to_hours(seconds):
    hours = seconds / 3600
    return int(hours)

#=========#
# MINUTES #
#=========#

def seconds_to_minutes(seconds, hours):
    seconds = seconds - 3600 * hours
    minutes = seconds / 60
    return int(minutes)

#=========#
# SECONDS #
#=========#

def seconds_remaining(seconds, minutes):
    return seconds % 60

#======#
# MAIN #
#======#

hours = 0
minutes = 0
seconds = 0
seconds = int(input("Enter the number of seconds"))
hours = seconds_to_hours(seconds)
minutes =  seconds_to_minutes(seconds, hours)
seconds = seconds_remaining(seconds, minutes)
print(hours, "hours", minutes, "minutes", seconds, "seconds")

