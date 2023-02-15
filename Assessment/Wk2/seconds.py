# Convert seconds into hours, minutes, seconds. 

##
#   Imports
# ##
from datetime import timedelta

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

print ( 'Time converter v0.1')
print ( '-' * 42 )

# Get the input of seconds
var_seconds = get_int("Enter Number of Seconds",int(1),int(86399))

# output the result 
tmp_conv=str(timedelta(seconds=var_seconds))

a_parts=tmp_conv.split(":")

# I noticed the Minutes value column was misaligned on the assignments layout, but assumed that was an oversight. 
print ( f'{"Input":6} {"Hours":>10} {"Minutes":>10} {"Seconds":>10} ')
print ( f'{var_seconds:<6} {int(a_parts[0]):10} {int(a_parts[1]):10} {int(a_parts[2]):10} ')
