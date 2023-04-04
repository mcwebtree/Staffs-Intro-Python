# metals

import os 
import pprint as pp

def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w") as fh_metals:
            fh_metals.write("beryllium 4 9.012\n")
            fh_metals.write("magnesium 12 24.305\n")
            fh_metals.write("calcium 20 20.078\n")
            fh_metals.write("strontium 38 87.62\n")
            fh_metals.write("barium 56 137.327\n")
            fh_metals.write("radium 88 226\n")

def read_file():
    global a_metals
    with open(file_name) as fh_metals:
        for line in fh_metals:  
            a_line = line.split()
            a_line[1] =int(a_line[1])
            a_line[2] = float(a_line[2])
            
            a_metals.append(a_line)

file_name = "alkaline_metals.txt"
a_metals = []
# do it
create_file()

read_file()

pp.pprint (a_metals)