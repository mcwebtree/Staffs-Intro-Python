## print this data

stuff={'Ford': ['Researcher',60000], 'Sara': ['Lecturer', 50000]}

for keys, values in stuff.items():
    print ( keys )
    for entry in values :
        print ( f"    {entry} " )
