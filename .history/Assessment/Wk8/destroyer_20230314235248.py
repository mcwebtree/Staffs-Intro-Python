# single ship battleship game. 

def init_board(bw, bh):
    board=[]
    for x in range(bh):
        board[x]=[]
        for y in range(bw):
            board[x][y]=" "
    return board 

def print_board(board, bw, bh):
    
    print ("  ", end='')
    for y in range(1,bw+1):
        print ( f' {y} ' )

    for x in board:
        print ( f'{x} ')
        for y in board[x]:
            print ( f'[{board[x][y]}]', end='')
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

print_board ( board )