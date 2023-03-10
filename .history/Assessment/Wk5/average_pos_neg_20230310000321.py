# Loop to handle 10 integer input and do maths. 

l_pos=[]
l_neg=[]

for i in range(10):
    tmp_in = int( input( f"Please enter integer [{i+1}/10]: ") )
    if tmp_in > int(0):
        l_pos.append(tmp_in)
    else:
        l_neg.append(tmp_in)

print ( f"Using the negative values {sorted(l_neg)} and positive values {sorted(l_pos)} " )
print ( f'The sum of the negative values is: {sum(l_neg)}')
print ( f'The sum of the positive values is: {sum(l_pos)}')
