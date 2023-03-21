# single ship battleship game. 

import pprint as pp

# Screen control params
UP = '\033[1A'
CLEAR = '\x1b[2K'
RESET = '\033[2J'
BLINKON = '\033[32;5m'
BLINKOFF = '\033[0m'
#print ( UP, end=CLEAR)

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

    for ship in ships:
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
    global exit_flag
    s_err=""

    while True:
        s_shot = input ( f"{s_err}Please enter your target (RC e.g. 10) [Q to exit]: ")

        if s_shot.upper() == "Q":
            exit_flag=1
            break

        shot_x = int( s_shot[0] ) - 1 
        shot_y = int( s_shot[1] ) - 1

        if (shot_x < 1 or shot_x > board_height) or (shot_y < 1 or shot_y > board_width):
            s_err = "Invalid Coordinates"
            continue

        if board[shot_x][shot_y] != " ":
            s_err = "Coordinates already targeted"
            continue
        
        break 

    return s_shot
     

# inits 
# // only works up to a 9x9 currently 
board_width=5
board_height=5

# program quit flag
exit_flag = 0 

# Build the array of ships 
ships=[]
ships.append({"Length": 2, "Locn": [[2,2],[2,3]]})

#print ( ships )

#   Setup the game
board,targets = init_board( board_width , board_height )
place_ships ( )
#pp.pprint ( board ) 

print_board (  )

# Let the target practice commence
while True:
    s_shot = get_shot()
    if s_shot.upper() == 'Q':
        print ( "Thanks for playing " )
        break 
    take_shot ( s_shot )
    print_board ( )
