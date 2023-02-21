# Do some maths on a number

#helpers 

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


#inits 
a_nums=[]

# Header
print ( "Welcome to the number regurgitator ")
print ( "-" * 50 )

print ( "Please enter as many numbers as you want.\nTo finish the list enter 0.")

# get input 
tmp_var=(get_int("Enter an integer between 1 and 100: ",1,100))
while tmp_var >0:
    a_nums.append(tmp_var)
    tmp_var=(get_int("Enter an integer between 1 and 100: ",1,100))


print ( "You entered: ")
print ( a_nums) 
