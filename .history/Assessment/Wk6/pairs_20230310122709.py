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
RESET = '\033[2J'
#print ( UP, end=CLEAR)

# inits 
def build_grid():
    d_grid=[]
    for i in range(4):
        d_grid.append([{"val": "", "matched": 0, "check" : 0},
                    {"val": "", "matched": 0, "check" : 0},
                    {"val": "", "matched": 0, "check" : 0},
                    {"val": "", "matched": 0, "check" : 0}])

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

def print_grid(d_grid, i_clear=0, i_reveal = 0 ):
    if i_clear == 1 :
        #print ( UP * 5, end=CLEAR)
        print (RESET)

    print ( "  0 1 2 3" )
    for i in range(4):
        print ( i, end = " " )
        for j in range(4):
            if d_grid[i][j]["matched"]==1 or  d_grid[i][j]["check"]==1 or i_reveal==1:
                print (d_grid[i][j]["val"], end=" ")
            else:
                print ( "#", end = " " )
        print ("")
    
    print ("")

# more inits
i_matches=0
i_guesses=0
d_grid=build_grid()

print (RESET)
print_grid ( d_grid )

# Actually play the game 
while i_matches < 8:
    while True: 
        try: 
            loc1 = input ( "Please enter a location to flip (XY e.g 00) (ENTER to Quit) :" )
            if loc1=="": break
            if len(loc1) !=2:
                raise ValueError
            
            x1=int(loc1[0])
            y1=int(loc1[1])
            if d_grid[x1][y1]["matched"]==1:
                print ( f"Location {loc1} is already flipped " )
            else:
                d_grid[x1][y1]["check"]=1
                print_grid ( d_grid, 1 )
                break
        except ValueError:
            # Input failure
            print ("Invalid location entered")
        except: 
            # it failed 
            print ("Invalid location entered")
    if loc1=="": break

    while True: 
        try: 
            loc2 = input ( "Please enter a location to flip (x y) (ENTER to Quit) :" )
            if loc2=="": 
                break
            elif loc1==loc2:
                print ( "Cannot select the same location twice" )
                #x = input ("Press ENTER to continue")
            else:
                try2 = loc2.split(" ")
                x2=int(try2[0])
                y2=int(try2[1])
                if d_grid[x2][y2]["check"]==1 or d_grid[x2][y2]["matched"]==1:
                    print ( f"Location {try2} is already flipped " )
                else:
                    d_grid[x2][y2]["check"]=1
                    print_grid ( d_grid, 1 )
                    break
        except: 
            # it failed 
            print ("Invalid location entered")
            x=1
    if loc2=="": break

    if d_grid[x2][y2]["val"] == d_grid[x1][y1]["val"]:
        d_grid[x1][y1]["matched"]=1
        d_grid[x2][y2]["matched"]=1
        i_matches += 1
        print ( "Great job. Match confirmed! ")
    else :
        print ( f"Keep trying, only {8-i_matches} pairs left." )
        
    d_grid[x1][y1]["check"]=0
    d_grid[x2][y2]["check"]=0

    x = input ("Press ENTER to continue")

    print_grid ( d_grid, 1 )

    
    




