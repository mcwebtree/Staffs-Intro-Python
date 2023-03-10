# get 5 integers and reverse them. 

# inits
a_ints=["Values"]

print ("Number Sequence Reversal")
print ("========================")

print ( "Values Entered  :", end = " ")
for i in range(1, 6):
    tmp_in=int ( input ( "Enter an integer: " ) )
    print ( tmp_in, end=" " )
    a_ints[i]=tmp_in

print ("")
print ( a_ints )

print ( "Values Reversed :", end = " ")
for i in range (4, 0, -1):
    print ( a_ints[i], end=" " )
