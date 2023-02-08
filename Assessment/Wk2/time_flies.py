# Play around with a users age

# import modules
import sys 

# Params
f_valid=0

# Display header
print ( "Welcome to the Age Adjustor ")
print ( "-" * 40 )

# Get user input and validate
while f_valid!=1:
    var_age = ( input( f"Please enter your age: ") )
    
    # Allow a way out by entering an empty string to quit
    if var_age=="": 
        sys.exit( "Empty value detected - quitting." )

    try:
        int_age = int( var_age ) 
        f_valid=1
    except ValueError:
        print ( f"Invalid value entered, ({var_age}). Please try again." )
    except: 
        print ( "+++ Out of cheese error +++" )
    
# Calc the dates
int_last_year = int_age - 1
int_next_year = int_age + 1   

# output the results

print ( "-" * 40 )
print( f"Your current age is " + str(int_age) )
print( f"Before your last birthday you were " + str(int_last_year) )
print( f"After your next birthday you will be " + str(int_next_year) )
