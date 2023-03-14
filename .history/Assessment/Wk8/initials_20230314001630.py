# get a users initials from their name. 

# inputs
s_name = input ( "Please enter your name" )

# calcs
a_names = s_name.split(" ")

s_inits=""
for name in a_names :
    s_inits += name[0] + ". "

print ( f"Initials for {s_name} are {s_inits}" )
