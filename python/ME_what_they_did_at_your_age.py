#ME what they did at your age
#wtdaya = what they did at your age

#----------
#subprogram
#----------

def wtdaya():
    if age < 8:
        print("We don't have anyone of your age on our list, but remember it's never too late to do something amazing and never too early to start trying!")
    elif age == 8:
        print("at age 8, three-time Olimpic gold medal winner Wilma Rudolph walked for the first time")
    elif age == 9:
        print("at age 9, Mozart began composing symphonies")
    elif age == 10:
        print("at age 10, Stevie Wonder was sighned by Motown records")
    elif age == 11:
        print("at 11, Victoria van Meter was the first girl to fly across the US")
    elif age == 12:
        print("at 12, Steven Spielberg got his first movie camera")
    elif age == 13:
        print("at 13, Jordan Romero became the youngest person to summit Mount Everest")
    elif age == 14:
        print("at age 14, Laura Dekker sailed around the world solo")
    elif age == 15:
        print("at age, 15 Hanson Crockett Gregory claims to cut the centre out a doughnut to make the first ring doughnut")
    elif age == 16:
        print("at age 16, Lana del Rey released her first album, 'Born to die'")
    else:
        print("We don't have anyone of your age on our list, but remember it's never too late to do something amazing and never too early to start trying!")

#-----------
#mainprogram
#-----------

age = int(input("what age are you: "))
wtdaya()