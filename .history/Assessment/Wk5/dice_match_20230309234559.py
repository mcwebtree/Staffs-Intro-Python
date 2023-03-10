# throw 2 die until they match

import random

while True:
    die_a = random.randrange(1,6)
    die_b = random.randrange(1,6)
    print ( f"Dice A: {die_a}  Dice B: {die_b}")
    if die_a == die_b :
        print ( " Matched Pair Thrown ")
        break
    