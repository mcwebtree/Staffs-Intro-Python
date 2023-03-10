# Create a diamond of width 2 -> 40 

#inits
i_width = int(input( "Please enter the desired width: " ) )
i_max_width= ( 2 * i_width) - 1

print ( f"Creating a {i_width} character diamond  " )
print ( '-' * i_max_width )

for i in range( i_width - 1 ):
    i_indent = i_width - ( 2 * i ) - 1
    print ( i_indent ( " " * i_indent ) ( "* " * i ) )

print ( "* " * i_width )

for i in range( i_width - 1, 1, -1 ):
    i_indent = i_width - ( 2 * i ) - 1
    print ( i_indent ( " " * i_indent ) ( "* " * i ) )