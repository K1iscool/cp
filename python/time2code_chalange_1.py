# This program will generate lyrics for a personalised Jingle Bells carol.

# ----------------
# Constants
# ----------------

BELL_ASCII_ART = """			   			  		
				   _,--._
                                 ,'  _.._`.
                            ,^.,' ,-" _," ;
                   _,----.._\\|( _/,--"  ,<
                 ,'     ____(_))< ___..".  `.
                :  _,-"__,-" (_)-.      ,\\.  \
                :,'..-"  _,-")|(\\ `._.-"_,\\  \
                 `.__ ,-"    '-`'   \\.-"   Y  :
                 /  /:-...______...-:      |  |
                (  ( |-...______...-'      ;  ;_
                 \\ ,\\|              |     /,^/  ;._
                  `  .              .        _,'   ;
                     :              :    _,-'    ,"
                     '              ` ,-'     _,"
                    '                '    _,-"`.
                   ;`--...______,,,--":.-"     ;
                  :                    :  `..."
                  '---....______,,,,---'
                           :     ;
                            `.,."          
"""

# ----------------
# Subprograms
# ----------------

def word_chosing(carol):
    noun = input("please input a noun; ")
    animal = input("please input a animal; ")
    place_plural = input("please input a place in plural format; ")
    verb = input("please input a verb; ")
    carol = f"""Jingle bells, jingle bells, jingle all the way!
Dashing through the {noun}
On a one-{animal}-open-sleigh
O'er the {place_plural} we go
{verb} all the way."""
    print(carol)

# ----------------
# Main program
# ----------------
print(BELL_ASCII_ART)
print("welcome to the christmas carol maker")
carol = ""
word_chosing(carol)

