# Create a diamond of width 2 -> 40 

#inits
while True:   
    try:
        i_width = int(input( "Please enter the desired width between 2 and 40: " ) )
        
        # test the range is valid
        if i_width > 1 and i_width < 41 :
            i_max_width= ( 2 * i_width) - 1

            print ( f"Creating a {i_width} character diamond  " )
            print ( '-' * i_max_width )

            for i in range( 1, i_width  ):
                i_indent = (i_width - i) 
                #print ( str(i_indent), end="")
                print ( " " * i_indent, end="")
                print ( "* " * i ) 
            print ( "* " * i_width )
            for i in range( i_width - 1 , 0, -1 ):
                i_indent = (i_width - i) 
                #print ( str(i_indent), end="")
                print ( " " * i_indent, end="")
                print ( "* " * i )    
            break 
        
        else :
            print ( "Invalid width entered! " )
    except ValueError:
        s_err="Invalid entry detected - non integer! "
    # except:
    #     s_err="An unknown error occurred! "


