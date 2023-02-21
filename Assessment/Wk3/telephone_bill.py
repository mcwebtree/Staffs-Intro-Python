# Calculate a phone call cost. 

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
call_rate=int(15)
vat_rate=float(0.2) ## 20%

# Get user data
num_mins=get_int("Please enter the number of minutes used: ", 1, 9999)

# calcs
basic_charge = num_mins * call_rate  ## in pence
vat_charge = basic_charge * vat_rate ## again in pence

# output 
print ( f'Number of minutes used: {num_mins}')
print ( f'Basic call charge: £{(basic_charge/100):.2f}')
print ( f'VAT due: £ {(vat_charge/100):.2f}')  ## this spurious space after the £ was in the spec... 
print ( f'Total bill: £{((basic_charge+vat_charge)/100):.2f}')
