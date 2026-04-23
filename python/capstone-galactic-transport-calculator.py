#===================#
# CAPSTONE LVL4 GTC #
#===================#

#======#
# subs #
#======#

#======#
# HELP #
#======#

def help_page(running):
    print("""
Please call Voice and SSTV Downlink: 145.80
""")
    menu(running)

#=====#
# MAP #
#=====#

def zone_map(running):
    print("""
+======+===+=======+
| Zone | 1 | 3.0LY |
| Zone | 2 | 2.6LY |
| Zone | 3 | 1.3LY |
| Zone | 4 | 2.4LY |
| Zone | 5 | 0.9LY |
| Zone | 6 | 1.1LY |
| Zone | 7 | 6.2LY |
+------+---+-------+

For more information see help page
          """)
    menu(running)

#=================#
# FARE CALCULATOR #
#=================#

def fare_calc(running):
    print("This is the GTFC™ mathematical engine")
    start = int(input("Where are you starting from? "))
    stop = int(input("Where are you planing on stoping? "))
    zones_travelled = start - stop
    zones_travelled = abs(zones_travelled)
    total = 5 + zones_travelled * 2.5
    print(f"Your fare from Zone{start} to Zone{stop} is £{total:.2f}")
    menu(running)

#======#
# MENU #
#======#

def menu(running):
    if running:
        print("""
This is the GTFC™ menu please select one of the following options
1) calculate fare
2) galactic zone map
3) help page
4) quit""")
        option = input("")
        if int(option) == 1:
            fare_calc(running)
        elif int(option) == 2:
            zone_map(running)
        elif int(option) == 3:
            help_page(running)
        elif int(option) == 4:
            running = False
            quit()
        else:
            print("Sorry that wasn't a valid input")
            menu(running)

#======#
# main #
#======#
running = True
while running:
    print("Welcome to the Galactic Transport Fare calculator!™")
    menu(running)

