# calculate salary 

def calc_salary(s_name, s_type, *args):
    if s_type.upper()=="F":
        return args[0]
    else:
        return int(args[0])*int(args[1])
    
def do_emp():
    s_name=input("Enter employee name: ")
    s_type=input("Enter employee type ([F]ulltime/[P]arttime): ").upper()

    sal=""
    rate=""
    hours=""

    if s_type == "F":
        sal = input("Please enter basic salary: ")
        their_sal=calc_salary(s_name, s_type, sal)
    else :
        rate = input ( "Please enter hourly rate: ")
        hours = input ( "Please enter number of hours: ")
        their_sal=calc_salary(s_name, s_type, rate, hours)

    print ( f'{s_name} is {s_type} with sal {sal}, rate {rate}, hours {hours}')    
    print ( f'{s_name} has salary of {their_sal}')

do_emp()