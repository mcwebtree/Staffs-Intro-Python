# Repeat a character, n times. 

## Prints a character a specified number of times.
def character_print(s_char, i_reps):
    print ( s_char * i_reps )

# Do the do.
s_char = input( "Please enter the character you want repeating: ")
i_reps = int( input( "Please enter the number of repetitions you want: " ) )

print ( f"Repeating the character {s_char} {i_reps} times." )
print ( "" )

character_print ( s_char, i_reps )