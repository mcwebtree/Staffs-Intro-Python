# single ship battleship game. 

import pprint as pp

def init_board(bw, bh):
    board=[[' ' for j in range(bw)] for i in range(bh)]
    targets=[['M' for j in range(bw)] for i in range(bh)]
    return board,targets 

def print_board():
    print ("  ", end='')
    for y in range(board_width):
        print ( f' {y+1} ', end=' ' )
    print ( '' )

    for x in range(board_height):
        print ( str( x+1 ) + ' [' + '] ['.join(board[x]) + ']')
        
def place_ships():
    global targets

    i_len=ships[0]
    for ship in ships[1:]:
        for plot in ship["Locn"]:
            targets[plot[0]][plot[1]]="H"

def take_shot(shot_x, shot_y):
    global board
    board[shot_x][shot_y]=targets[shot_x][shot_y]
    if board[shot_x][shot_y]=="H":
        print ( f'Congratulations that was a hit' )
    else :
        print ( f'Unlucky, you missed that time' )

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
place_ships ( targets, ships )
#pp.pprint ( board ) 

print_board ( board, board_width, board_height )
print_board ( targets, board_width, board_height )

# Let the target practice commence
while True:

