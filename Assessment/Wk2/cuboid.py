#  Calculate cuboid stats

# helpers

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    return_value=int(0)
    int_val=int(-1)

    try:
        while not ((int_val >= min_int & int_val <= max_val)) :
            get_val=input(input_prompt + f" (Min: {str(min_int)} Max: {str(max_int)} Exit: 0)")
            int_val=int(get_val)

            ## exit if select 0
            if  int_val==0: 
                break
        
        return_value=int_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
    finally:
        return return_value



# params
min_int=int(1)
max_int=int(100)

print ( 'Welcome to the Cuboid Calculator' )
print ( '-' * 40 )

cub_width=get_int("Width  (cm): ")
cub_height=get_int("Height (cm): ")
cub_length=get_int("Length (cm): ")

print (type(cub_width))
print (type(cub_height))
print (type(cub_length))


if ( cub_width > int(0) and cub_height > int(0) and cub_length > int(0) ) :
    surface= 2 * ( ( cub_width * cub_height ) + ( cub_height * cub_length ) + ( cub_length * cub_width ) )
    volume = cub_height * cub_length * cub_width

    print ( f'Width: {cub_width} Height: {cub_height} Length: {cub_length} ')
    print ( f'Surface area: {str(surface)} Volume: {str(volume)} ' )


else :
    
    print ( f'Width: {cub_width} Height: {cub_height} Length: {cub_length} ')
    print ("Invalid dimensions provided. Cannot calculate answers.")



