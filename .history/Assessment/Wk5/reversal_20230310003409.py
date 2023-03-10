# enter an integer and reverse it

# helpers

# integer reverser keeping to an int. 
def flip_me(i_num):
    i_flip=0
    while i_num != 0:
        i_last = i_num % 10
        i_flip = ( i_flip * 10 ) + i_last
    return i_flip 

# inits
s_err=""

# user input
while True:   
    try:
        tmp_in = int( input( f"{s_err}Please enter integer between 2 and 10 digits (-1 to exit): ") )
        # if the length matches, exit 
        if  tmp_in == int(-1) :
            break 

        if tmp_in > 9 and tmp_in < 10000000000 :
            tmp_flip=""
            print ( f'{tmp_in} reversed is {flip_me(tmp_flip)}')
        else :
            s_err = "Invalid length! "
    except ValueError:
        s_err="Invalid entry! "
    # except:
    #     s_err="An unknown error occurred! "

