#simulate coin flip multiple times
import random
import sys

# declarations
intHeads=0
intTails=0

# args

strName=str(sys.argv[1])
intLoops=int(sys.argv[2])

#intro
print("Hi "+strName)
print("Starting test with "+ str(intLoops)+" loops")

#run tests
num=random.randint(0,1)
if num==0:
    coin_face="Heads :)"
else :
    coin_face="Tails :("

for i in range(intLoops):
    num=random.randint(0,1)
    if num==0:
        coin_face="Heads :)"
        intHeads+=1
    else :
        coin_face="Tails :("
        intTails+=1
    ret1=str(i)+" "+coin_face
    #print(ret1)

# calc averages
avgHeads=round((intHeads/intLoops)*100,2)
avgTails=round((intTails/intLoops)*100,2)

# output results
print("Heads: "+str(intHeads)+" ("+str(avgHeads)+"%)  Tails:"+str(intTails)+" ("+str(avgTails)+"%)")