# play with the world (globals)

# function 
def sums():
    global gVal
    gVal = (g1 + g2) * g3

# variables
g1 = 1
g2 = 2
g3 = 3
gVal = 0 

print ( "Before: " + str(gVal) )
sums()
print ( "After: " +  str(gVal) )