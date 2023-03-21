# single ship battleship game. 

import pprint as pp

def init_board(bw, bh):
    board=[[' ' for j in range(bw+1)] for i in range(bh+1)]
    return board 

def print_board(board, bw, bh):
    print ("  ", end='')
    for y in range(bw):
        print ( f' {y} ', end=' ' )
    print ( '' )

    for x in range(bw):
        print ( str( x ) + ' [' + '] ['.join(board[x]) + ']')
        

# inits 
# // only works up to a 9x9 currently 
board_width=5
board_height=5

# Build the array of ships 
ships=[1]
ships.append({"Length": 2, "Locn": [[2,2],[2,3]]})

print ( ships )

#   
#   Setup the game
#
board=init_board(board_width, board_height)
pp.pprint ( board ) 
print_board ( board, board_width, board_height )