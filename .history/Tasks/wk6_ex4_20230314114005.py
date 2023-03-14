# calculate salary 

def calc_salary(s_name, s_type, base_salary = int(0), hourly_rate=int(0), num_hours = int(0) ):
    if s_type.upper()=="F":
        return base_salary
    else:
        return hourly_rate*num_hours
    
def do_emp():
    s_name=input("Enter employee name: ")
    s_type=input("Enter employee type ([F]ulltime/[P]arttime): ").upper()

    sal=""
    rate=""
    hours=""

    if s_type == "F":
        sal = input("Please enter basic salary: ")
    else :
        rate = input ( "Please enter hourly rate: ")
        hours = input ( "Please enter number of hours: ")
    
    print ( f'{s_name} has salary of {calc_salary(s_name, s_type, sal, rate, hours)}')

do_emp()