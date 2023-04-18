# calculate ticket costs for theatre bookings

import time

# helpers

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

## function to get an Y/N with error checking
def get_y_n ( input_prompt ):
    return_value=""
    var_val = "Z" 

    try:
        while not ( var_val == "Y" or var_val == "N" ) :
            var_val=input(input_prompt + f" (Y/N) ").upper()
            
            ## exit if select 0
            if  var_val=='': 
                break
        
        return_value=var_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '" + var_val + "'" ) 
    finally:
        return return_value


# inits
costs = { 'Adult' : 10.50 , 'Child' : 7.30 , 'Conc' : 8.40 }
num_kids_for_free_adult = 10
discount = { 'minimum_spend': float(100.00), 'discount' : int(10) }
the_p_n_p_cost = float(2.34)

# welcome
print ( 'Thank you for shopping at TicketMistress' )
print ( '=' * 40 )

# get values 
num_in_party = get_int( "Please enter the number of tickets required: " , 1 , 150 )
num_adults = get_int( "How many full price adults? " , 1 , num_in_party)
num_conc = get_int( "How many concessions? ", 0, (num_in_party - num_adults))
is_collection = get_y_n( "Will you be collecting the tickets? " )

# calcs
num_kids=num_in_party-num_adults-num_conc
num_free_adults= int( num_kids / num_kids_for_free_adult )
num_free_conc = 0

# can't give away more seats than you've got! 
# roll down free adults to concessions if there is a surplus 
if num_free_adults > num_adults: 
    num_spare_adults = num_free_adults - num_adults
    num_free_adults=num_adults
    num_free_conc=num_spare_adults

if num_free_conc>num_conc:
    num_free_conc=num_conc

# calc how many are paying
num_paying_adults=num_adults-num_free_adults
num_paying_conc=num_conc-num_free_conc

# check they have adults to cover the kids
if num_kids == num_in_party:
    print ("Invalid order. All children must have at least one adult attending.")
    print ("Please try to place your order again. ")
else:
    # output the receipt. 
    ticket_values={"Adult": 0, "Conc": 0 , "Child": 0}
    ticket_values["Adult"] = num_paying_adults * costs["Adult"]
    ticket_values["Conc"] = num_paying_conc * costs["Conc"]
    ticket_values["Child"] = num_kids * costs["Child"]

    ttl_bill_pre_discount = ( ticket_values["Adult"] ) + \
                            ( ticket_values["Conc"] ) + \
                            ( ticket_values["Child"] )

    # calculate discount
    discount_percentage = 0
    bill_discount = 0
    if ttl_bill_pre_discount > discount["minimum_spend"] : 
        discount_percentage=discount["discount"]
        bill_discount = ttl_bill_pre_discount * ( discount_percentage / 100 )

    # calculate delivery

    if is_collection == "Y" :
        p_n_p_cost=0
    else :
        p_n_p_cost=the_p_n_p_cost

    bill_total=ttl_bill_pre_discount - bill_discount + p_n_p_cost

    # generate bill reference 
    bill_ref=str(time.time())[3:10]

    # output bill 
    print ( )
    print ( "The Sandford Paladium")
    print ( "*" * 21 )
    print ()

    print ( f'{num_in_party} Tickets for Snakes! The Musical' )
    print ( f'{"Order Ref: " + bill_ref:>36}')
    print ( '-' * 36 )
    if is_collection == "Y" :
        print ( "*" * 9, "   COLLECTION   ", "*" * 9 )
        print ( '-' * 36 )

    if num_adults > 0:
        print ( f'{num_adults:3} {"Adult":12} ' )
        if num_paying_adults > 0 : print ( ' ' * 12 , f'{num_paying_adults:3} @ £{costs["Adult"]:5.2f} = £{ ticket_values["Adult"]:7.2f} ')
        if num_free_adults > 0 : print ( ' ' * 12 , f'{num_free_adults:3} @ £{0:5.2f} = £{0:7.2f} ')
        print ( "" )

    if num_conc > 0: 
        print ( f'{num_conc:3} {"Concessions":12} ' )
        if num_paying_conc > 0 : print ( ' ' * 12 , f'{num_paying_conc:3} @ £{costs["Conc"]:5.2f} = £{ ticket_values["Conc"]:7.2f} ')
        if num_free_conc > 0 : print ( ' ' * 12 , f'{num_free_conc:3} @ £{0:5.2f} = £{ 0:7.2f} ')
        print ( "" )

    if num_kids > 0 : 
        print ( f'{num_kids:3} {"Child":12} @ £{costs["Child"]:5.2f} = £{ ticket_values["Child"]:7.2f} ')
        s_plural=""
        if num_free_adults+num_free_conc > 1:
            s_plural="s" 
        if num_kids > 9 : print ( f"    (Includes {num_free_adults+num_free_conc} free chaperone{s_plural})")
        print ( "" )

    print ( ' ' * 27, '=' * 8 )

    if discount_percentage > 0 :
        print ( ' ' * 9 , f'{"Sub Total":17} £{ttl_bill_pre_discount:7.2f}' )
        print ( ' ' * 9 , f'{"Discount (" + str(discount["discount"]) + "%)":17} £{bill_discount:7.2f}' )
        print ( ' ' * 27, '-' * 8 )
        
    if p_n_p_cost > 0 :
        print ( ' ' * 9 , f'{"Postage":17} £{p_n_p_cost:7.2f}' )
        print ( ' ' * 27, '-' * 8 )
        
    print ( ' ' * 9 , f'{"Total":17} £{bill_total:7.2f}' )
    print ( ' ' * 27, '=' * 8 )