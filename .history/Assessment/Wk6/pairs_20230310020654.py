# kims game 

# imports
from datetime import datetime
import time

# ESCAPE SEQUENCE	CURSOR MOVEMENT
# \033[<L>;<C>H	Positions the cursor. Puts the cursor at line L and column C.
# \033[<N>A	Move the cursor up by N lines.
# \033[<N>B	Move the cursor down by N lines.
# \033[<N>C	Move the cursor forward by N columns.
# \033[<N>D	Move the cursor backward by N columns.
# \033[2J	Clear the screen, move to (0,0)
# \033[K	Erase the end of line.

UP = '\033[1A'
CLEAR = '\x1b[2K'

print (" Overwrite task ")
print ( "=" * 20 )

print (  )
for i in range(120):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(1)
    print ( UP, end=CLEAR)
