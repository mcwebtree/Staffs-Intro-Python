# Calculate paint coverage and can box amounts. 

# import packages
import math

# params
fl_coverage = 5.1 # m2 of wall 
# I'm using a dictionary as an array of dimensions, I mused on a list or a tuple too, but went for dict for clarity
t_can_dims = { "Diameter": 15, "Height" : 30 } # cm
t_box_dims = { "Length": 0.60, "Width": 0.30, "Height": 0.35 }  # meters (I assume). 
t_hall_dims = { "Length": 40, "Width": 30, "Height": 3.4 } # meters

# ASSUMPTIONS
# The hall has no doors
# The hall has no windows
# The floor and ceiling aren't being painted

# Calculate amount of paint required
# ( 2 x length + 2 x width ) * height
int_hall_wall_area = ( (( t_hall_dims["Length"] * 2 ) + (t_hall_dims["Width"] * 2)) * t_hall_dims["Height"] )
int_cans_required = math.ceil ( int_hall_wall_area / fl_coverage )
t_cans_per_box = { "ByLength" : math.floor ( t_box_dims["Length"] / ( t_can_dims["Diameter"] / 100 ) ),
                    "ByWidth" : math.floor ( t_box_dims["Width"] / ( t_can_dims["Diameter"] / 100 ) ),
                    "ByHeight" : math.floor ( t_box_dims["Height"] / ( t_can_dims["Height"] / 100 ) )
                }
int_cans_per_box = t_cans_per_box["ByWidth"] * t_cans_per_box["ByLength"] * t_cans_per_box["ByHeight"]
int_full_boxes = math.floor ( int_cans_required / int_cans_per_box )
int_loose_cans = int_cans_required % int_cans_per_box

print ( 'Welcome to the Shaggy Dog Paint calculator')
print ( '-' * 42 )
print ( f'Using paint cans with diameter {t_can_dims["Diameter"]}cm and height {t_can_dims["Height"]}cm providing coverage of {fl_coverage}m2.')
print ( f'Painting a hall with length {t_hall_dims["Length"]}m, width {t_hall_dims["Width"]}m and height {t_hall_dims["Height"]}m.')
print ( f'This will require {int_cans_required} cans of paint.')
print ( f'Supplying {int_cans_per_box} cans per box this will require {int_full_boxes} boxes and {int_loose_cans} loose cans.')