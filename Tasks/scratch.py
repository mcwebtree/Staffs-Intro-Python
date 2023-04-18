
# my code 

arr = [["J" for i in range(4)],
       ["Q" for i in range(4)],
       ["K" for i in range(4)],
       ["A" for i in range(4)],]

# my print 

print ("  1 2 3 4")
for i in range(4):
    print ( str(i+1), end= " " )
    for j in range(4):
        print ( "#", end=" " )
        #print ( arr[i][j], end=" " )
    print ( "" )

print ( "" )

print ("  1 2 3 4")
for i in range(4):
    print ( str(i+1), end= " " )
    for j in range(4):
        #print ( "#", end=" " )
        print ( arr[i][j], end=" " )
    print ( "" )



# a,b = "1 2 3 4".split()
# print ( a )
# print ( b )