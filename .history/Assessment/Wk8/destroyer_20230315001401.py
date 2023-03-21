# single ship battleship game. 

import pprint as pp

def init_board(bw, bh):
    board=[[' ' for j in range(bw)] for i in range(bh)]
    targets=[['M' for j in range(bw)] for i in range(bh)]
    return board,targets 

def print_board(board, bw, bh):
    print ("  ", end='')
    for y in range(bw):
        print ( f' {y+1} ', end=' ' )
    print ( '' )

    for x in range(bw):
        print ( str( x+1 ) + ' [' + '] ['.join(board[x]) + ']')
        
def place_ships(targets, ships):
    i_len=ships[0]
    for ship in ships[1:]:
        for plot in ship["Locn"]:
            targets[plot[0]][plot[1]]="H"
    return targets

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
targets = place_ships ( targets, ships )
#pp.pprint ( board ) 

print_board ( board, board_width, board_height )
print_board ( targets, board_width, board_height )