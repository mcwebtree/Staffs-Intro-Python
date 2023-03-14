# Do maths 

def add_vals( i_1, i_2 ) :
    print ( f'{i_1} + {i_2} = {i_1+i_2}')

def sub_vals( i_1, i_2 ) :
    print ( f'{i_1} - {i_2} = {i_1-i_2}')

def multiply_vals( i_1, i_2 ) :
    print ( f'{i_1} * {i_2} = {i_1*i_2}')

def divide_vals( i_1, i_2 ) :
    print ( f'{i_1} / {i_2} = {i_1/i_2}')

def get_remaind_vals( i_1, i_2 ) :
    print ( f'{i_1} % {i_2} = {i_1%i_2}')

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    return_value=int(0)
    int_val=int(min_val-1)

    try:
        while not ((int_val >= min_val and int_val <= max_val)) :
            get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: 0)")
            
            int_val=int(get_val)
            
            ## exit if select 0
            if get_val==int ( 0 ): 
                break
                    
        return_value=int_val
    except:
        print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
    finally:
        return return_value

print ( "Welcome to the Fun Calc 2000 ")
print ( "=============================")

i_val_1 = int ( get_int( "Please enter the first non zero integer: ", -999999, 999999 )) 
if i_val_1 != 0:
    i_val_2 = int ( get_int( "Please enter the second non zero integer: ", -999999, 999999  )) 
    if i_val_2 != 0:
        print ( "Please select from the following operations: \n"
                " 1. Add \n"
                " 2. Subtract \n"
                " 3. Multiply \n"
                " 4. Divide \n"
                " 5. Remainder "
                )

        s_op = input( "Enter operation [1-5] :")

        print ( "=============================")
        print ( "The calculator says ", end="")

        match s_op: 
            case "1":
                add_vals ( i_val_1, i_val_2 )
            case "2":
                sub_vals ( i_val_1, i_val_2 )
            case "3":
                multiply_vals ( i_val_1, i_val_2 )
            case "4":
                divide_vals ( i_val_1, i_val_2 )
            case "5" :
                get_remaind_vals (i_val_1, i_val_2 )
    else: 
        print ( "Quit! ")
else: 
    print ( "Quit! ")