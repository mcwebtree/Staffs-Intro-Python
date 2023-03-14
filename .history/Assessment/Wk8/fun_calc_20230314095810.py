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


print ( "Welcome to the Fun Calc 2000 ")
print ( "=============================")

i_val_1 = int ( input("Please enter the first value: " )) 
i_val_2 = int ( input("Please enter the second value: " )) 

print ( " Please select from the following operations: \n"
        " 1. Add \n"
        " 2. Subtract \n"
        " 3. Multiply \n"
        " 4. Divide \n"
        " 5. Remainder "
        )

s_op = input( "Enter operation [1-5] :")

match s_op: 
    case "1":
        add_vals ( i_val_1, i_val_2 )
    case "2":
        sub_vals ( i_val_1, i_val_2 )
    case "3":
        multiply_vals ( i_val_1, i_val_2 )
    case "4":
        sub_vals ( i_val_1, i_val_2 )
    case "5" :
        get_remaind_vals (i_val_1, i_val_2 )