# list swip swapper

def swap( l_vals ):
    l_vals.reverse()
    return l_vals

def print_int_list( l_vals ):
    for i in l_vals:
        print ( i, end=" ")
    print ( "" )


s_vals = input ( "Please enter 2 integers separated by a space: " )
print ( f'You entered            : "{s_vals}"')
l_vals = s_vals.split()
print ( f'I found these values   :', end=" " )
print_int_list ( l_vals )
l_vals_r = swap ( l_vals )
print ( f'I swapped these values :', end=" " )
print_int_list ( l_vals_r )
