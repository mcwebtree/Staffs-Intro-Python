# calculate total cost of living 

##
#  Helpers 
##

## function to get a float with error checking
def get_float(input_prompt, min_val=float(0.01), max_val=float(100.00)):
    return_value=float(0.0)
    float_val=float(-1)

    try:
        while not ((float_val >= min_val and float_val <= max_val)) :
            get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: 0)")
            float_val=float(get_val)

            ## exit if select 0
            if  float_val==0: 
                break
        
        return_value=float_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '{get_val}'" ) 
    finally:
        return return_value

print ( 'Monthly Cost adder upper')
print ( '-' * 25 )

#Input
rent=get_float("Rent per month",float(0.01),float(9999.99))
gas=get_float("Gas payment per month",float(0.01),float(9999.99))
elec=get_float("Electric payment per month",float(0.01),float(9999.99))
water=get_float("Water payment per month",float(0.01),float(9999.99))
council=get_float("Council tax payment per month",float(0.01),float(9999.99))
total = rent + gas + elec + water + council

# Output
print ( 'Your monthly expenses are:')
print ( f'{"Rent:":16}£{rent:8.2f}')
print ( f'{"Gas:":16}£{gas:8.2f}')
print ( f'{"Electricity:":16}£{elec:8.2f}')
print ( f'{"Water:":16}£{water:8.2f}')
print ( f'{"Council Tax:":16}£{council:8.2f}')
print ( "=" * 25)
print ( f'{"Total:":16}£{total:8.2f}')
print ( "=" * 25)