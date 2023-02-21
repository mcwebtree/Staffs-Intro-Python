
# Importing primes function
# From primePy Library

from primePy import primes

for num in range(2,100):
    if num % 2 == 0:
        print ( "Found an even number: ", num )
    else :
        print ( "This one is odd: ",num)

    if primes.check(num) :
        print ( " AND it's a prime number!! ")

    if num > 10: 
        break

            
    