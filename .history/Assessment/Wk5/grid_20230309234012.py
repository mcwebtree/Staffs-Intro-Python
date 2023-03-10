# create a grid of * from dimensions entered by the user

i_width = int(input( "Please enter the desired width: " ) )
i_height = int(input( "Please enter the desired height: " ) )

print ( f"Creating a grid {i_height} x {i_width}")
print ( '-' * i_width)

for i in range(i_height):
    print ( "* " * i_width)