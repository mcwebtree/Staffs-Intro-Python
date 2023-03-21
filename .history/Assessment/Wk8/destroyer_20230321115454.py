# single ship battleship game. 

import pprint as pp
import random as r

# Screen control params
UP = '\033[1A'
UP2 = '\033[2A'
CLEAR = '\x1b[2K'
RESET = '\033[2J'
BLINKON = '\033[32;5m'
BLINKOFF = '\033[0m'
REVON = "\033[7m"
REVOFF = "\033[0m"
#print ( UP, end=CLEAR)

def init_board(bw, bh):
    print ( f'Creating a board {bw}*{bh} ' )
    board=[[' ' for j in range(bw)] for i in range(bh)]
    targets=[['M' for j in range(bw)] for i in range(bh)]
    return board,targets 

def print_board(f_live = 1):
    if f_live==0:
        this_board=targets
    else:
        this_board=board

    print (RESET)
    
    s_output += f" There are {num_placed_ships} ships in total.\n"
    s_output += f" There are {parts_to_sink} remaining parts to hit.\n\n"

    s_output += REVON + "   "
    for y in range(board_width):
        s_output += f'  {y+1} '
    s_output += REVOFF + '\n'

    for x in range(board_height):
        s_output += REVON + ' ' + str( x+1 ) + ' ' + REVOFF + ' [' + '] ['.join(this_board[x]) + ']\n'

    s_output = s_output.replace( "[H]" , REVON + '[H]'+ REVOFF )
    print ( s_output )
        
#/// This places a pre defined array of ships in the grid. 
def place_ships():
    for ship in ships:
        place_ship ( ship )

#/// This places a single ship in the grid. 
def place_ship(a_ship):
    global targets
    global parts_to_sink

    for plot in a_ship["Locn"]:
        targets[plot[0]][plot[1]]="H"
        parts_to_sink +=1


#/// This creates ships as it goes based on the parameters in the ships array
#/// The maximum length of a ship is the board (width / 2 ) + 1
def create_ships():
    global targets

    ships_to_place = len(auto_ships)
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
                place_ship ({"Length": ship['Length'], "Locn": [ship_locn['Locn']]})
                ships_placed += 1
               
    return ships_placed

#// go to the board and find a home for a ship
def find_space(length):
    ret_val = {"Success": 0, "Locn": []}
    found_spaces = 0
    
    i_iters=0
    i_max_iters = 1000
    start_x = r.randrange(0, board_width-1)
    start_y = r.randrange(0, board_height-1)

    #// Decide where you're going and go get something.
    dir = r.choice( ['N', 'E', 'S', 'W'] )
    
    while True:
        i_iters += 1
        print ( f'Testing {start_x},{start_y}' )
        if targets[start_x][start_y]=="M":
            ret_val['Locn'].append([start_x, start_y])
            x, y = start_x, start_y
            found_spaces = 1
            done_swap = 0 

            while found_spaces < length:
                x,y=next_space(x, y, dir)
                # if its off the board, or already occupied then flip direction and try again
                if x < 0 or x >= board_width or y < 0 or y >= board_height or targets[x][y] == "H":
                    done_swap += 1
                    dir = swap_direction( dir )
                    x, y = start_x, start_y
                    # if you've tried to swap already, fail. 
                    if done_swap > 1:            
                        ret_val['Locn'].clear()
                        x,y = -1,-1
                        break
                    else:
                        continue 
                else :
                    ret_val['Locn'].append([x, y])
                    found_spaces += 1

            if found_spaces == length: # if it worked, mark as success 
                ret_val['Success']=1   
                # exit the infinite while to return the status. 
                break
            else: 
                # Space is not free so fail this route and try again .       
                ret_val['Locn'].clear()
                
                if i_iters >= i_max_iters:
                    ret_val['Success']= -1 # mark as timeout failure 
                    break
                else:
                    start_x = r.randrange(0, board_width-1)
                    start_y = r.randrange(0, board_height-1)
                    i_iters += 1

        else: 
            start_x = r.randrange(0, board_width-1)
            start_y = r.randrange(0, board_height-1)
            dir = r.choice( ['N', 'E', 'S', 'W'] )
            found_spaces = 0
            done_swap = 0 
            i_iters += 1

        if i_iters >= i_max_iters:
            ret_val['Success']= -2 # mark as timeout failure 
            break

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

def next_space(x, y, dir):
    if dir == 'N':
        y += -1
    elif dir == 'E':
        x += 1
    elif dir == 'S':
        y += 1
    elif dir == 'W':
        x += -1
    return x, y

def take_shot(s_shot):
    global board
    global parts_to_sink

    # remember to subtract 1 from the shot to shift the array into the right location
    shot_x = int( s_shot[0] ) - 1 
    shot_y = int( s_shot[1] ) - 1

    board[shot_x][shot_y]=targets[shot_x][shot_y]

    print_board ( )

    if board[shot_x][shot_y]=="H":
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
     

# inits 
# // only works up to a 9x9 currently 


# program quit flag
# used by functions to flag the need to quit the program
exit_flag = 0 

parts_to_sink=0

s_game_type = input ( "Do you want the [S]imple (set in assignment) game or [A]utomatic play? [S/A]")

if s_game_type == "S":
    board_width=5
    board_height=5
    # Build the array of ships 
    ships=[]
    ships.append({"Length": 2, "Locn": [[2,2],[2,3]]})
else:
    user_board = input("Please enter the board dimensions (e.g. 5x5, 4x9) [MAX 9x9]: ")
    board_width, board_height = int(user_board[0]), int(user_board[2])

    # Build the automatic ships array
    auto_ships=[]
    auto_ships.append({'Length': 5, 'Qty': 1})
    auto_ships.append({'Length': 4, 'Qty': 1})
    auto_ships.append({'Length': 3, 'Qty': 2})
    auto_ships.append({'Length': 2, 'Qty': 3})

#print ( ships )

#   Setup the game
board,targets = init_board( board_width , board_height )

if s_game_type == "S":
    place_ships ( )
    num_placed_ships = len(ships)
else: 
    num_placed_ships = create_ships ( )

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
        print ( f"{BLINKON}Congrats!{BLINKOFF} You've taken them all out.")
        break
