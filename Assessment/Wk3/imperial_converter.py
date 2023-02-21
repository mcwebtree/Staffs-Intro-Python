# converts imperial values to metric

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


# inits
inch_factor  = float(2.54)

print ( "Imperial converter ")
print ( "-" * 25 )

# get user input 
print ( 'Please enter your height in feet and inches')
usr_height_feet = get_int("Enter feet :",1,9)
usr_height_inches = get_int("Enter inches : ",1,12)

# calcs
usr_h_in = ( usr_height_feet * 12 ) + usr_height_inches
usr_h_cm = usr_h_in * inch_factor

# output 

print ( f"User's imperial height is { usr_height_feet }' { usr_height_inches }\" " )
print ( f"Height in kilometres: { usr_h_cm / 100000 }")
print ( f"Height in metres: { usr_h_cm / 100 }")
print ( f"Height in centimetres: { usr_h_cm  }")
print ( f"Height in millimetres: { usr_h_cm * 10 }")


