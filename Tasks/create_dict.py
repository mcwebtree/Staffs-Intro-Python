# create a dictionary from user input
 
import pprint

emps = {}

while 1==1 :
    new_key=input( "Enter the Employee Name: (enter 0 to exit) " )
    if (new_key == "0"): 
        break 
    new_role=input( "Enter the Employee Role:  (enter 0 to exit)" )
    if (new_role == "0"): 
        break 
    new_salary=input ( "Enter the Employee Salary:  (enter 0 to exit) ")
    if (new_salary == "0"): 
        break 
    emps[new_key] = [new_role, new_salary]

pp1=pprint.PrettyPrinter( compact=False)

pp1.pprint ( emps )

    
