# play with the world (globals)

g1 = 1
g2 = 2
g3 = 3
gVal = 0 

def sums():
    global gVal
    gVal = (g1 + g2) * g3

print ( "Before: " + gVal )
sums()
print ( "After: " +  gVal )