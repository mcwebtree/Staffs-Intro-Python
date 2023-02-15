# calculate the qty and price of a list of shopping items. 

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
        print ( f"Invalid '{input_prompt}' value entered '{get_val}'" ) 
    finally:
        return return_value

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


# Inits
ar_items=[{"item" : "Peaches", "unit" : "one of", "qty" : int(0), "price" : float(0.0)},
          {"item" : "Beans", "unit" : "can of", "qty" : int(0), "price" : float(0.0)},
          {"item" : "Chicken pieces", "unit" : "packet of", "qty" : int(0), "price" : float(0.0)},
          {"item" : "Socks", "unit" : "pair of", "qty" : int(0), "price" : float(0.0)},
          {"item" : "Water", "unit" : "bottle of", "qty" : int(0), "price" : float(0.0)}]

## Begin 
print ( f'Welcome to the Shopping List Wizard')
print ( '-' * 47)
#print ( 'Please enter the Quantity and Price for each item.\n')

ttl_qty=int(0)
ttl_price=float(0)

## Get the qty and price
for shop_item in ar_items:
    #print ( f'Item     : {shop_item["item"]}')
    tmp_qty=get_int(f'Quantity of {shop_item["item"]} ({shop_item["unit"]}) :',0,10)
    tmp_price=get_float(f'Price of {shop_item["item"]}  ({shop_item["unit"]}) : £')
    shop_item["qty"]=tmp_qty
    shop_item["price"]=tmp_price
    ttl_qty+=tmp_qty
    ttl_price+=(tmp_qty*tmp_price)
    print ( f'{tmp_qty} {shop_item["unit"] + " " + shop_item["item"]:25} @ £{tmp_price:6.2f} = £{(tmp_qty*tmp_price):6.2f}')
    
print ( '-' * 39, '=' * 7)
print( f"You've ordered {ttl_qty} items totalling       £{ttl_price:6.2f}")
print ( '-' * 39, '=' * 7)

