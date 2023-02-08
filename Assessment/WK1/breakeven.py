# calculate break even point for business

# Params
dbl_cost = 20.00
dbl_sale = 40.00
dbl_fixed_costs = 50000.00

# Calculate profit
dbl_profit = dbl_sale - dbl_cost

# Get sale count to meet fixed costs
int_BE_sales = int( dbl_fixed_costs / dbl_profit )

# check if there is a residual amount and if so increase the min qty
# by one as you can't sell a fraction of a product
if ( ( dbl_profit * int_BE_sales ) < dbl_fixed_costs ) :
    int_BE_sales +=1

# Output the results
print ( "Welcome to the Widget Factory break even calculator" )
print ( "-" * 55 )
print( f'Widgets cost £{dbl_cost:.2f} and sell for £{dbl_sale:.2f}')
print( f'We make a profit of {dbl_profit:.2f} per widget.' ) 
print( f'Our fixed costs are £{dbl_fixed_costs:.2f}.' )
print( f'Therefore we need to sell {int_BE_sales} items to break even.')