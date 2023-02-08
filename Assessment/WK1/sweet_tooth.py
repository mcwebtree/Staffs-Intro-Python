# Calculate the improbable situation of teacher distributing a daft number of sweets 

# params
int_sweets=40
int_students=14

# calculate distibution values 
int_teacher_loot=int_sweets % int_students
int_per_student=( int_sweets - int_teacher_loot ) / int_students

print ( 'Welcome to Wonkas Sweet Distribution Calculator' )
print ( '-' * 50 )
print ( f'The teacher started with {int_sweets} sweets.' )
print ( f'Each student receives {int_per_student:.0f} sweets.' )
print ( f'The teacher is forced to keep {int_teacher_loot} sweets.' )
