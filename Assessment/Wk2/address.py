# create an address label format

# modules
import sys 

# params
str_salutation="Mr and Mrs"

# get user input - NO validation 

str_name = input ( "Please enter your last name" )

var_house_number = input ( "Please enter your house number" )
if var_house_number.isdigit():
    int_house_number = int ( var_house_number )
else:
    sys.exit("Invalid house number ")

str_road = input ( "Please enter your road name" )
str_town = input ( "Please enter your town" )

print ( "Address Label Creator" )
print ( "-" * 22)
print ( f'{str_salutation} {str_name},\n{str(int_house_number)}, {str_road}\n{str_town}')