# kims game 

# imports
import random as r 

# ESCAPE SEQUENCE	CURSOR MOVEMENT
# \033[<L>;<C>H	Positions the cursor. Puts the cursor at line L and column C.
# \033[<N>A	Move the cursor up by N lines.
# \033[<N>B	Move the cursor down by N lines.
# \033[<N>C	Move the cursor forward by N columns.
# \033[<N>D	Move the cursor backward by N columns.
# \033[2J	Clear the screen, move to (0,0)
# \033[K	Erase the end of line.

UP = '\033[1A'
CLEAR = '\x1b[2K'
#print ( UP, end=CLEAR)

# inits 
def build_grid(i_output = 0):
    d_grid=[]
    for i in range(4):
        d_grid.append([{"val": "", "matched": 0},
                    {"val": "", "matched": 0},
                    {"val": "", "matched": 0},
                    {"val": "", "matched": 0}])

    l_cards=[]
    for i in range(4):
        l_cards.append("J")
        l_cards.append("Q")
        l_cards.append("K")
        l_cards.append("A")

    r.shuffle(l_cards)

    for i in range(4):
        for j in range(4):
            d_grid[i][j]["val"]=l_cards.pop()
        
    return d_grid

def print_grid(d_grid, i_reveal = 0 ):
    print ( "  0 1 2 3" )
    for i in range(4):
        print ( i, end = " " )
        for j in range(4):
            print (d_grid[i][j]["val"], end=" ")
        print ("")

# Actually play the game 
d_grid=build_grid(1)
print_grid ( d_grid )
