# get 5 integers and reverse them. 

# inits
a_ints=[]

print ("Number Sequence Reversal")
print ("========================")

print ( "Values Entered:", end = " ")
for i in range(5):
    tmp_in=int ( input ( "Enter an integer: " ) )
    print ( tmp_in, end=" " )
    a_ints.append(tmp_in)

print ("")

print ( "Values Reversed:", end = " ")
for i in range (4, 0, -1):
    print ( a_ints[i], end=" " )
    