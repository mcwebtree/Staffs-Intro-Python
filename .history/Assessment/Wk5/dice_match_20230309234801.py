# throw 2 die until they match

import random

i_loop = 0

while True:
    i_loop +=1
    die_a = random.randrange(1,6)
    die_b = random.randrange(1,6)
    print ( f"Roll {i_loop} -> Dice A: {die_a} Dice B: {die_b}")
    if die_a == die_b :
        print ( f"Matched Pair Thrown on Roll {i_loop}" )
        break
    