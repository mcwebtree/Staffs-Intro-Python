# enter an integer and reverse it

# helpers

# integer reverser keeping to an int. 
def flip_me(i_num):
    i_flip=0
    while i_num != 0:
        i_last = i_num % 10
        i_flip = ( i_flip * 10 ) + i_last
        i_num = i_num // 10
    return i_flip 

# inits
s_err=""

# user input
while True:   
    try:
        tmp_in = int( input( f"{s_err}\nPlease enter an integer between 2 and 10 digits (-1 to exit): ") )
        # if the length matches, exit 
        if  tmp_in == int(-1) :
            break 

        if tmp_in > 9 and tmp_in < 10000000000 :
            print ( f'{str(tmp_in):10} reversed is {str(flip_me(tmp_in)):10}')
            s_err=""
        elif tmp_in < 0 :
            s_err = "Invalid value! "
        else :
            s_err = "Invalid length! "
    except ValueError:
        s_err="Invalid entry! "
    # except:
    #     s_err="An unknown error occurred! "

