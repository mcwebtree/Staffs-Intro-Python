
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

