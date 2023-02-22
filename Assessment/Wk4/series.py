# identify positive / negative integers 

# inits 
i_pos=0
i_neg=0
a_values=[]

# user entry
for i in range(5):
    tmp_var=int(input("Please enter a non Zero integer value: "))
    
    a_values.append(str(tmp_var))

    if tmp_var > 0: 
        i_pos += tmp_var
    else :
        i_neg += tmp_var

print ( "For the values " + ",".join(a_values) )
print ( "Sum of positive integers: " + str(i_pos) )
print ( "Sum of negative integers: " + str(i_neg) )