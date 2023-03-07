# Dictionary tests

import pprint 
import json

dict = {"bob": {"cost": 1234, "nickname": "Roger"}, \
            "Dave" : {"cost": 5678, "nickname": "Big D" }, \
            "Bert" : {"cost": 9922, "nickname": "DangerB"}, \
            "Sandra": {"cost": "12.55", "nickname:": "Triple S"}}

test = "bob"

print ( " Testing Print / Dict ")
pp1 = pprint.PrettyPrinter(indent=2, width=50, compact=False )
pp1.pprint( dict )



print ( "Testing for " + test)

if test in dict.keys() :
    print ( f"Found {test}" )
else :
    print ( f'NOT found {test}' )