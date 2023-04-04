
from lorem_text import lorem as lt

print ( "Generating Text File" )
print ( "--------------------" )
with open("text.txt", "w") as fh_1:
    for i in range(10):
        fh_1.write ( lt.sentence() + '\n' )

print ( "\nReading back file contents" )
print ( "--------------------------" )
with open("text.txt", "r") as fh_1:
    for line in fh_1:
        print ( line.strip() )
