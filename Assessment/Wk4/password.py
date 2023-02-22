# Test a password against a stored value

#inits 
valid_pass="CorrectHorseBatteryStaple"

# get user entry
test_pass=input("Please enter the password: ")

if valid_pass.upper()==test_pass.upper():
    print ( "Welcome to the Realms of XKCD" )
