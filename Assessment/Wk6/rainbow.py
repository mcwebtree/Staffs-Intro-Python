# output rainbow colours on demand. 

# inits 
a_rb = ['Rainbow Colours','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
a_scb = ["0;0;0m","255;0;0m", "255;165;0m", "255;255;0m", "0;255;0m", "0;0;255m", "255;85;255m", "170;0;170m"]
a_scf = ["255;255;255m","255;255;255m", "0;0;0m", "0;0;0m", "0;0;0m", "255;255;255m", "255;255;255m", "255;255;255m"]

s_fg = "\033[38;2;"
s_bg = "\033[48;2;"

# this prints the text with the right background
def print_colour(i):
    s_col_on=s_fg + a_scf[i]
    s_col_off=s_fg + a_scf[0]
    s_bg_on=s_bg + a_scb[i]
    s_bg_off=s_bg + a_scb[0]
    
    print ( f"{s_bg_off}{s_col_off}{i}:{s_col_on}{s_bg_on} {a_rb[i]:^10} {s_bg_off}{s_col_off}")
    pass

while True:
    i_val = int ( input ( "Enter a value between 1 and 7 : (-1 to exit)") )

    # exit condition
    if i_val == int(-1):
        break

    # required output condition
    if i_val > 0 and i_val < 8 :
        print_colour ( i_val )
    
    # this is not in the assignment but I added it to ease debugging with the colour combinations
    elif i_val == 0:
        print ( "You found the Easter Egg. \nA Double Rainbow :)")

        for i in range(7,0,-1):
            print_colour ( i )
        print ("")
        for i in range(1,8):
            print_colour ( i )
        
    # error message
    else:
        print ( "Invalid option selected")
    
