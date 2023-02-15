## distance calculator for calculating distances. 

##
#  Helpers 
##

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    return_value=int(0)
    int_val=int(-1)

    try:
        while not ((int_val >= min_val and int_val <= max_val)) :
            get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: 0)")
            int_val=int(get_val)

            ## exit if select 0
            if  int_val==0: 
                break
        
        return_value=int_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
    finally:
        return return_value



# The formula you will need to perform the calculation is:
# 𝑠=𝑢𝑡+ 1/2(𝑎𝑡2)
# where
# 𝑠 = distance
# 𝑢 = initial velocity
# 𝑡 = time taken
# 𝑎 = acceleration

print ( 'Distance Calculator ' )
print ( '-' * 42 )

## get values 
val_u = get_int("Initial Velocity")
val_t = get_int("Time taken")
val_a = get_int("Acceleration")

val_s = (val_u * val_t) + (0.5 * val_a * (val_t * val_t))

print ( f'An object travelling with initial velocity {val_u} m/s')
print ( f'Accelerating at a constant rate of {val_a} m/s/s')
print ( f'For {val_t} seconds ')
print ( f'Will have travelled {val_s} meters ')

