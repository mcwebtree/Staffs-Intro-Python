# Get a users initials from their name. 
# 

import re

# inputs
s_name = input ( "Please enter your name" )

# strip leading and following spaces
s_name=s_name.strip(" ")

# calcs
a_names = re.split("\s+", s_name)

s_inits=""
for name in a_names :
    name_part=name.split("-")
    np_inits=[]
    for np in name_part:
        np_inits.append(np[0].upper() )
    
    s_inits +="-".join(np_inits) + ". "

print ( f"Initials for {s_name} are {s_inits}" )
