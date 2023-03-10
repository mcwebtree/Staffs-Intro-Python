# Loop to handle 10 integer input and do maths. 

l_pos=[]
l_neg=[]

for i in range(10):
    tmp_in = input( "Please enter an integer: ")
    if tmp_in > 0:
        l_pos.append(tmp_in)
    else:
        l_neg.append(tmp_in)

print ( f"Using the values [{l_neg.sort()}, {l_pos.sort()}] " )
print ( f'The sum of the negative values is: {sum(l_neg)}')
print ( f'The sum of the positive values is: {sum(l_pos)}')
