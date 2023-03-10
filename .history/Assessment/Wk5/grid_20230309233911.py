# create a grid of * from dimensions entered by the user

i_width = int(input( "Please enter the desired width: " ) )
i_height = int(input( "Please enter the desired height: " ) )

for i in range(i_height):
    print ( "* " * i_width)