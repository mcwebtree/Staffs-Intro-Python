## Calculate an employees salary 

## inits
sal_lecturer=int(50000)
sal_lecturer_allowance=int(10000)
sal_lecturer_ot=int(0)
sal_clerk=int(30000)
sal_clerk_ot=int(20)
sal_clerk_allowance=int(0)

# header
print (f'Welcome to the Salary Sum System 2000')
print ('-' * 50)

# Get params from user
print ("Please enter staff name")
staff_name=input("Enter Name   :")
print ("Please enter staff type. L for Lecturer, C for Clerk")
staff_type=input("Type (L or C) :")
ot_hours=int(0)
salary=int(0)

if staff_type.upper()=="L":
    base_salary=sal_lecturer
    ot_rate=sal_lecturer_ot
    allowance=sal_lecturer_allowance
    staff_label="Lecturer"

elif staff_type.upper()=="C":
    ot_hours=int(input("Please enter OT hours: "))
    base_salary=sal_clerk
    ot_rate=sal_clerk_ot
    allowance=sal_clerk_allowance
    staff_label="Clerk"

else :
    staff_label="Unknown"
    base_salary=int(0)
    ot_rate=int(0)
    allowance=int(0)
    ot_hours=int(0)

salary=base_salary
salary+=(ot_hours*ot_rate)
salary+=allowance

#  Output result 
print (f'{staff_name} is a {staff_label}')
print (f' Base Salary : £{base_salary:8} ')
print (f' OT Hours    : £{ot_hours:8}')
print (f' OT Rate     : £{ot_rate:8}')
print (f' Allowance   : £{allowance:8}')
print (f' Total Salary: £{salary:8}')
