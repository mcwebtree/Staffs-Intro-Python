# output rainbow colours on demand. 

# inits 
a_rb = ['Rainbow Colours','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

while True:
    i_val = int ( input ( "Enter a value between 1 and 7 : (-1 to exit)") )
    if i_val == int(-1):
        break

    if i_val > 0 and i_val < 8 :
        print ( f"{i_val}: {a_rb[i_val]}")
        