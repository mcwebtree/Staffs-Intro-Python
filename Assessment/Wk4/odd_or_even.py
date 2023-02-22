# Calculate if an entered value is odd or even.

test_val=int(input("Please enter a positive integer: "))

if test_val % 2 == 0 :
    print ( str(test_val) + " is EVEN" )
else :
    print ( str(test_val) + " is ODD" )

##Sticking in a 1 liner
print ( "EVEN EVEN EVEN" if test_val % 2 == 0 else "ODD ODD ODD" )