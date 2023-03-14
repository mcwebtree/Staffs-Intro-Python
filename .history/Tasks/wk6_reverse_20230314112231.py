# reverse a string 

def rev_str( my_string ):
    lst1=list(my_string)
    lst1.reverse()
    return "".join(lst1)

def rev_str_2( my_string ):
    return my_string[::-1]

s_val=input("Please enter a string: ")
print ( f'{s_val} reversed is {(rev_str(s_val))}')
print ( f'{s_val} reversed is {(rev_str_2(s_val))}')