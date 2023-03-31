## Insertion sort implementation

import os
import sys

sys.path.append(os.path.abspath('..\\inc\\'))
import helpers as h

## Direction is D for Descending, pretty much anything else for Ascending
def ins_sort(l_data, direction = "D"):
    for i in range(1,len(l_data)):
        tmp_val=l_data[i]
        j=i-1

        # build the test
        if direction=="D":
            s_test=f"{l_data[j]}<{tmp_val}"
        else:
            s_test=f"{l_data[j]}>{tmp_val}"

        while j >=0 and eval(s_test):
            l_data[j+1] = l_data[j]
            j -= 1
                
            # build the test
            if direction=="D":
                s_test=f"{l_data[j]}<{tmp_val}"
            else:
                s_test=f"{l_data[j]}>{tmp_val}"
        l_data[j+1]=tmp_val
    return l_data

l_test_data=[] # [2,5,3,6,2,67,3,5,7,3,2,5,76,3,2,65,765,2,8,3,7]
a_direction={"A":"Ascending",
              "D":"Descending"}

for i in range(5):
    tmp_int = h.get_int("Please enter an integer: ",1,9999)
    l_test_data.append(tmp_int)

s_sort =""
while s_sort!="A" and s_sort != "D":
    s_sort = input ("Please select the direction of sort, [A]scending or [D]escending: ").upper()

print ("You provided: ")
print (l_test_data)
print ( f"You selected sorting {a_direction[s_sort]}")
l_sorted = ins_sort(l_test_data, s_sort)
print ( "Sorted that looks like: ")
print (l_sorted)
