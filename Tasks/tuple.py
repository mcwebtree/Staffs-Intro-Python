# do tuple stuff

tup=("abc","bcd","1","2","3","4",5,6,7,8,9)
print (tup)

tup2=(tup)
#print ("tup2: " + ','.join(tup2))

print ( "tup is tup2: " + str(tup is tup2))
print ( "tup == tup2: " + str(tup == tup2))

tup3=tuple(str(val) for val in tup)
print ( tup3 )
print ("tup3: " + ', '.join(tup3))

print ( "tup is tup3: " + str(tup is tup3))
print ( "tup == tup3: " + str(tup == tup3))

tup4=tuple(tup)
print ( "tup is tup4: " + str(tup is tup4))
print ( "tup == tup4: " + str(tup == tup4))
