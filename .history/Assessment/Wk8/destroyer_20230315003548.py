# single ship battleship game. 

import pprint as pp

# Screen control params
UP = '\033[1A'
CLEAR = '\x1b[2K'
RESET = '\033[2J'
BLINKON = '\033[32;5m'
BLINKOFF = '\033[0m'
#print ( UP, end=CLEAR)

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    ## used to show the parent code that its exited not finished
    global exit_flag 

    return_value=int(0)
    int_val=int(min_val-1)

    while True:
        try:
            while not ((int_val >= min_val and int_val <= max_val)) :
                get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: Q)")
                if get_val.upper() == "Q":
                    exit_flag=1
                    get_val=int( 0 )
                    break 

                int_val=int(get_val)
                
                ## exit if select 0
                if int_val==int ( 0 ): 
                    break

            return_value=int_val
            break
        except:
            print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
    
    return return_value


def init_board(bw, bh):
    board=[[' ' for j in range(bw)] for i in range(bh)]
    targets=[['M' for j in range(bw)] for i in range(bh)]
    return board,targets 

def print_board(f_live = 1):
    if f_live==0:
        this_board=targets
    else:
        this_board=board

    print (RESET)
    
    print ("  ", end='')
    for y in range(board_width):
        print ( f' {y+1} ', end=' ' )
    print ( '' )

    for x in range(board_height):
        print ( str( x+1 ) + ' [' + '] ['.join(this_board[x]) + ']')
        
def place_ships():
    global targets

    i_len=ships[0]
    for ship in ships[1:]:
        for plot in ship["Locn"]:
            targets[plot[0]][plot[1]]="H"

def take_shot(s_shot):
    global board

    # remember to subtract 1 from the shot to shift the array into the right location
    shot_x = int( s_shot[0] ) - 1 
    shot_y = int( s_shot[1] ) - 1

    board[shot_x][shot_y]=targets[shot_x][shot_y]
    if board[shot_x][shot_y]=="H":
        print ( f'Congratulations that was a hit' )
    else :
        print ( f'Unlucky, you missed that time' )
    input ("Press ENTER to continue")

def get_shot():
    
    exit_param=0
    while True:
        s_shot= input ( "Please enter your target (RC e.g. 10) [Enter to exit]: ")
        shot_x = int( s_shot[0] ) - 1 
        shot_y = int( s_shot[1] ) - 1

    return s_shot, exit_param
     

# inits 
# // only works up to a 9x9 currently 
board_width=5
board_height=5

# Build the array of ships 
ships=[1]
ships.append({"Length": 2, "Locn": [[2,2],[2,3]]})

#print ( ships )

#   Setup the game
board,targets = init_board( board_width , board_height )
place_ships ( )
#pp.pprint ( board ) 

print_board (  )

# Let the target practice commence
while True:
    s_shot,exit_param = get_shot()
    if s_shot=='':
        print ( "Thanks for playing " )
        break 
    take_shot ( s_shot )
    print_board ( )
