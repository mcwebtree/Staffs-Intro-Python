# single ship battleship game. 

import pprint as pp

def init_board(bw, bh):
    board=[[' ' for j in range(bw)] for i in range(bh)]
    return board 

def print_board(board, bw, bh):
    
    print ("  ", end='')
    for y in range(1,bw+1):
        print ( f' {y} ' )

    for x in board:
        print ( f'{x} ')
        print ( x + '[' + '] ['.join(board[x]) + ']')
        # for y in board[x]:
        #     print ( f'[{board[x][y]}]', end='')
        print ( "" )

# inits
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

print ( board )

print_board ( board, bw, bh )