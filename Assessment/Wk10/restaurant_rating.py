# Calculate a restaurant rating 

# define
REDON = "\033[31m" #	Red text.
ORANGEON = "\033[38;2;255;165;0m"
YELLOWON = "\033[38;2;255;255;0m"
GREENON = "\033[32m" # 	Green text.
COLOUROFF = "\033[0m"	#Reset special formatting (such as colour).

# Custom Errors
class OutOfRange( ValueError ):
    pass

class OutOfRangeLow (OutOfRange):
    pass

class OutOfRangeHigh (OutOfRange):
    pass

def average(lst):
    return sum(lst) / len(lst)

def percentage(numitems, ttlitems):
    return (numitems / ttlitems) * 100

def get_colour(i_val):
    if i_val < 1.5:
        s_colour = REDON
    elif i_val < 3:
        s_colour = ORANGEON
    elif i_val < 4: 
        s_colour = YELLOWON
    else:
        s_colour = GREENON
    return s_colour

l_votes=[[], 0, 0, 0, 0, 0]

# get input
while True:
    try:
        s_val = input ("Please enter your rating [1 (lowest) - 5 (highest)] (-1 to exit) :")
        i_val = int( s_val )

        if i_val == -1:
            break
        elif i_val < 1:
            raise OutOfRangeLow
        elif i_val > 5:
            raise OutOfRangeHigh
        else:
            l_votes[0].append(i_val)
            l_votes[i_val] += 1
            
    except OutOfRange as err:
        if isinstance(err,OutOfRangeLow):
            print ("If you think the rating is that low, please contact the Councils Public health or Trading standards as appropriate.")
            print ("1 is the lowest you can record here, please try again.")
        elif isinstance(err,OutOfRangeHigh):
            print ("We're happy you think the restaurant is that good.")
            print ("Please contact the restaurant and let them know.")
            print ("5 is the highest you can record here, please try again.")
        i_val=""
    except ValueError as err:
        print (f'Invalid value entered [{s_val}], please ensure you enter an integer between 1 and 5')
        i_val=""

if (len(l_votes[0]) == 0):
    print ( "No ratings were entered :(")
else:
    i_votes=len(l_votes[0])
    if i_votes == 1:
        print (f"There was only {i_votes} rating entered")
    else:
        print (f"There were {i_votes} ratings entered")
        
    for i in range (1, 6):
        s_colour=get_colour(i)
        print (f"{s_colour}{'*' * i:>6}{COLOUROFF}: {l_votes[i]:>4}  [{percentage(l_votes[i],i_votes):6.2f}%]")
    
    i_avg=average(l_votes[0])
    s_colour=get_colour(i_avg)
        
    print( f'The overall rating is {s_colour} {i_avg:.1f} {COLOUROFF}')
