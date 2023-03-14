# join names

def join_names(*names):
    return " ".join(names)

a = input ( "Please enter first name")
b = input ( "Please enter last name")
print (f'Full name is {join_names(a, b)}')
