# Loop to handle 10 integer input and do maths. 

import statistics as s

l_pos=[]
l_neg=[]

for i in range(10):
    s_err=""
    while True:
        try:
            tmp_in = int( input( f"{s_err}Please enter integer [{i+1}/10]: ") )
            break
        except ValueError:
            s_err="Invalid entry! "
        except:
            s_err="An unknown error occurred! "

    if tmp_in < int(0):
        l_pos.append(tmp_in)
    else:
        l_neg.append(tmp_in)

if len(l_neg) > 0 :
    print ( f"Using the negative values {sorted(l_neg)}" )
    print ( f'The sum of the negative values is    : {sum(l_neg):8}')
    print ( f'The average of the negative values is: {s.mean(l_neg):8}')
else :
    print ( "There were no negative numbers entered")

print ("")

if len(l_pos) > 0 :
    print ( f"Using the positive values {sorted(l_pos)} " )
    print ( f'The sum of the positive values is    : {sum(l_pos):8}')
    print ( f'The average of the positive values is: {s.mean(l_pos):8}')
else :
    print ( "There were no positive numbers entered")
