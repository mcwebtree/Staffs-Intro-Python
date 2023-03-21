# single ship battleship game. 

## DEBUG FLAG
f_debug = 1

import pprint as pp
import random as r
import re

# Screen control params
UP = '\033[1A'
UP2 = '\033[2A'
CLEAR = '\x1b[2K'
RESET = '\033[2J'
BLINKON = '\033[32;5m'
BLINKOFF = '\033[0m'
REVON = "\033[7m"
REVOFF = "\033[0m"
REDON= "\033[31m" #	Red text.
GREENON = "\033[32m" # 	Green text.
COLOUROFF = "\033[0m"	#Reset special formatting (such as colour).
#print ( UP, end=CLEAR)

########################################
#
#   Row == Y == Height == R
#   Col == X == Width  == C
#
########################################

def init_board(bw, bh):
    print ( f'Creating a board {bw}*{bh} ' )
    board=[[' ' for j in range(bw)] for i in range(bh)]
    targets=[['-' for j in range(bw)] for i in range(bh)]
    return board,targets 

def print_board(f_live = 1):
    if f_live==0:
        this_board=targets
    else:
        this_board=board

    print (RESET)
    
    s_output = f"There are {num_placed_ships} ships in total.\n"
    s_output += f"There are {parts_to_sink} remaining part(s) to hit.\n\n"

    s_output += REVON + " R  C"
    for x in range(board_width):
        s_output += f'  {x+1} '
    s_output += '  C ' + REVOFF + '\n'

    for y in range(board_height):
        s_output += REVON + ' ' + str( y+1 ) + '  ' + REVOFF + '  [' + '] ['.join(this_board[y]) + ']\n'
    s_output += REVON +" R  " 
    s_output += REVOFF +'\n' 

    #// replace with RegEx
    pattern = r'\[[A-Z]\]'
    s_output = re.sub(pattern, lambda match: REDON + match.group() + COLOUROFF , s_output)
    pattern = r'\[\-\]'
    s_output = re.sub(pattern, lambda match: GREENON + match.group() + COLOUROFF , s_output)

    print ( s_output )
        
#/// This places a pre defined array of ships in the grid. 
def place_ships():
    for key, ship in ships.items():
        place_ship ( key, ship )

#/// This places a single ship in the grid. 
def place_ship( s_id, a_ship ):
    global targets
    global parts_to_sink
    global ships_placed

    if f_debug > 1:
        print (" Placing ship : ")
        pp.pprint(a_ship)

    for plot in a_ship["Locn"]:
        targets[plot[0]][plot[1]]=s_id
        parts_to_sink +=1
    ## update to say ship placed. 
    ships_placed += 1

#/// This creates ships as it goes based on the parameters in the ships array
#/// The maximum length of a ship is the board (width / 2 ) + 1
def create_ships():
    global targets

    ships_placed = 0

    i_max_size=(board_width // 2) + 1
    for ship in auto_ships:
        if ship["Length"] > i_max_size:
            # skip ships too large for the board
            continue
        else:
            #// create the ship and place it 
            ship_locn = find_space ( ship['Length'] )
            if ship_locn['Success']==1:
                new_ship={"Length": ship['Length'], "Locn": ship_locn['Locn']} 
                ships[ship_ids[ships_placed]]= new_ship
                place_ship ( [ship_ids[ships_placed]], new_ship )
                ships_placed += 1
               
    return ships_placed

#// go to the board and find a home for a ship
def find_space(length):
    if f_debug > 0:
        print ( f"Finding space for a ship {length} long" )
    
    ret_val = {"Success": 0, "Locn": []}
    found_spaces = 0
    
    i_iters=0
    i_max_iters = 1000
    start_r = r.randrange(0, board_height-1)
    start_c = r.randrange(0, board_width-1)

    #// Decide where you're going and go get something.
    dir = r.choice( ['N', 'E', 'S', 'W'] )
    
    while True:
        i_iters += 1
        
        if f_debug > 1:
            print ( f'Testing {start_r},{start_c}' )

        if targets[start_r][start_c]=="-":
            ret_val['Locn'].append([start_r, start_c])
            yr, xc = start_r, start_c
            found_spaces = 1
            done_swap = 0 

            while found_spaces < length:
                yr, xc =next_space(yr, xc , dir)
                # if its off the board, or already occupied then flip direction and try again
                if xc < 0 or xc >= board_width or yr < 0 or yr >= board_height or targets[yr][xc] != "-":
                    done_swap += 1
                    dir = swap_direction( dir )
                    yr, xc = start_r, start_c
                    # if you've tried to swap already, fail. 
                    if done_swap > 1:            
                        ret_val['Locn'].clear()
                        break
                    else:
                        continue 
                else :
                    ret_val['Locn'].append([yr, xc])
                    found_spaces += 1

            if found_spaces == length: # if it worked, mark as success 
                ret_val['Success']=1   
                # exit the infinite while to return the status. 
                break
            else: 
                # Space is not free so fail this route and try again .       
                ret_val['Locn'].clear()
                
                if i_iters >= i_max_iters:
                    ret_val['Success']= -1 # mark as iterations failure 
                    break
                else:
                    start_r = r.randrange(0, board_height-1)
                    start_c = r.randrange(0, board_width-1)
                    i_iters += 1

        else: 
            start_r = r.randrange(0, board_height-1)
            start_c = r.randrange(0, board_width-1)
            dir = r.choice( ['N', 'E', 'S', 'W'] )
            found_spaces = 0
            done_swap = 0 
            i_iters += 1

        if i_iters >= i_max_iters:
            ret_val['Success']= -2 # mark as iterations failure 
            break

    if f_debug > 1:
        print ( ret_val )
   
    #// just quit and return the values. 
    return ret_val

#/// Stolen from ChatGPT (v4) and adapted to see how it can write a function. 
#/// I can write it a few other ways, but thought I'd keep this one, its a bit overly complex but works.
def swap_direction(direction):
    # Create a dictionary to map the values to their translated values
    translation_dict = dict([('N', 'S'),('S', 'N'), ('E', 'E'), ('W', 'E')])
    direction = direction.upper()

    # Swap the direction if it exists in the translation dictionary
    if direction in translation_dict:
        return translation_dict[direction]
    else:
        return direction

def next_space(yr, xc, dir):
    if dir == 'N':
        yr += -1
    elif dir == 'E':
        xc += 1
    elif dir == 'S':
        yr += 1
    elif dir == 'W':
        xc += -1
    return yr, xc

def take_shot(s_shot):
    global board
    global parts_to_sink

    # remember to subtract 1 from the shot to shift the array into the right location
    shot_r = int( s_shot[0] ) - 1 
    shot_c = int( s_shot[1] ) - 1

    board[shot_r][shot_c]=targets[shot_r][shot_c]

    print_board ( )

    if board[shot_r][shot_c]!="-":
        parts_to_sink -=1
        print ( f'Congratulations that was a hit' )
    else :
        print ( f'Unlucky, you missed that time' )

    #input ("Press ENTER to continue")

def get_shot():
    global exit_flag
    s_err=""

    while True:
        if s_err > '':
            print_board ()

        s_shot = input ( f"{s_err}Please enter your target (RC e.g. 10) [Q to exit]: ")

        # deal with premature enter key hitting
        if s_shot == "":
            s_err =""
            continue 

        if s_shot.upper() == "Q":
            exit_flag=1
            break

        if len(s_shot) != 2:
            s_err = f"Invalid Coordinates {s_shot} \n "
            continue

        shot_x = int( s_shot[0] ) - 1 
        shot_y = int( s_shot[1] ) - 1

        if (shot_x < 0 or shot_x >= board_height) or (shot_y < 0 or shot_y >= board_width):
            s_err = f"Invalid Coordinates {s_shot} [{str(shot_x)},{str(shot_y)}]\n "
            continue

        if board[shot_x][shot_y] != " ":
            s_err = "Coordinates already targeted\n "
            continue
        
        break 

    return s_shot 

def check_exit():
    f_check=input("Are you sure you wish to quit? (Y/N) :").upper()
    return f_check

# inits 
# // only works up to a 9x9 currently 


# program quit flag
# used by functions to flag the need to quit the program
exit_flag = 0 

parts_to_sink=0
ships_placed = 0
ship_ids = "ABCDEFGHIJKLMNOP"

# use S to match the assignment brief e.g. 5x5 board with 1 x 2 space ship in known location
s_game_type = input ( "Do you want the [S]imple (set in assignment) game or [A]utomatic play? [S/A]: ")
s_game_type = s_game_type.upper()

ships={}

if s_game_type == "S":
    board_width=5
    board_height=5
    # Build the array of ships 
    ships["A"] = ({"Length": 2, "Locn": [[2,2],[2,3]]})
else:
    # this doesn't bother with any input validation. 
    # I could use my get_int helper here. 
    # invalid input with crash the program
    user_board = input("Please enter the board dimensions RxC (e.g. 5x5, 4x9) [MIN 4x4, MAX 9x9]: ")
    board_height, board_width = int(user_board[0]), int(user_board[2])
    
    # sanitise sizes 
    if board_width < 4: board_width=4
    if board_width > 9: board_width=9
    if board_height < 4: board_height=4
    if board_height > 9: board_height=9

    # Build the automatic ships array
    auto_ships=[]
    auto_ships.append({'Length': 5, 'Qty': 1})
    auto_ships.append({'Length': 4, 'Qty': 1})
    auto_ships.append({'Length': 3, 'Qty': 2})
    auto_ships.append({'Length': 2, 'Qty': 3})

#   Setup the game
board,targets = init_board( board_width , board_height )

if f_debug > 1:
    pp.pprint ( board )
    pp.pprint ( targets )
    a = input ("Press ENTER to continue: ")

# on automatic you need to create the ships to place
if s_game_type == "A":
    create_ships ( )
else:
    place_ships ( )

num_placed_ships = len(ships)

if f_debug > 0:
    pp.pprint ( ships )
    pp.pprint ( targets )
    a = input ("Press ENTER to continue: ")

print_board (  )

# Let the target practice commence
while True:
    s_shot = get_shot()
    if s_shot.upper() == 'Q':
        print_board ( 0 )
        print ( "Thanks for playing " )
        break 
    take_shot ( s_shot )

    if parts_to_sink == 0:
        print ( f"\n{BLINKON}Congrats!{BLINKOFF} You've taken them all out.\n\n")
        break
