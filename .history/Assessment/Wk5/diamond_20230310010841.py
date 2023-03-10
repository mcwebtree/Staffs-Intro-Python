# Create a diamond of width 2 to 40 

#inits

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

    else :
        print ( f"Invalid width entered! ({i_width})" )
except ValueError:
    print ( "Invalid entry detected - non integer! " )
except:
    print ( "An unknown error occurred! " )


