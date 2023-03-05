# check for vowels

#inits
tup_tests=('a','e','i','o','u')
tup_found=()
tup_notfound=()

test_word=input("Please enter the test word: ").lower()

print ( f'Testing the word {test_word}')

for tc in tup_tests :
    if tc in test_word :
        num_hits=test_word.count(tc)
        tup_found+=(str(num_hits)+'*'+tc,)
        #print ( "Does contains " + tc)
    else:
        tup_notfound += (tc,)
        #print ("Does NOT contain " + tc)
        
print ( "Found " + ', '.join(tup_found) )
print ( "No " + ','.join(tup_notfound) )
