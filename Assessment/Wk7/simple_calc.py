# A Simple Calculator

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    return_value=int(0)
    int_val=int(-1)

    try:
        while not ((int_val >= min_val and int_val <= max_val)) :
            get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: 0) :")
            int_val=int(get_val)

            ## exit if select 0
            if  int_val==0: 
                break
        
        return_value=int_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
    finally:
        return return_value
    
# Get user input
val_1 = get_int ( "Please enter your first number: ")
if val_1 != 0:     
    val_2 = get_int ( "Please enter your second number: ")
    if val_2 != 0:
        s_op = "#"
        while not s_op in ["+", "-","*","/"]:
            s_op = input ( "Please enter your operator (+,-,*,/): ")

        print ( f'Your sum in {val_1} {s_op} {val_2} and the answer is {eval(str(val_1) + s_op + str(val_2))}')