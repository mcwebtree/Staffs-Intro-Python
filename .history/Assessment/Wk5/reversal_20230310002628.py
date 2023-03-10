# enter an integer and reverse it

# inits
s_err=""

# user input
while True:   
    try:
        tmp_in = int( input( f"{s_err}Please enter integer between 2 and 10 digits (-1 to exit): ") )
        # if the length matches, exit 
        if  tmp_in == int(-1) :
            break 
        if (len(tmp_in) > 1 and len(tmp_in) < 11) :
            tmp_flip=""
            print ( f'{tmp_in} reversed is {tmp_flip}')
    except ValueError:
        s_err="Invalid entry! "
    except:
        s_err="An unknown error occurred! "

