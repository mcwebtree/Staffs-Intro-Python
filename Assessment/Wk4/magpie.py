# output a line from a riddle 

# inits 
a_line=["Magpie or MincePie? "]
a_line.append("One for sorrow")
a_line.append("Two for joy")
a_line.append("Three for a girl")
a_line.append("Four for a boy")
a_line.append("Five for silver")
a_line.append("Six for gold")
a_line.append("Seven for a secret never to be told")

# get user selection - note there is basic input validation 
try:
    usr_selection = int(input("Enter your chosen line from 1 to 7 : "))
    if usr_selection > 0 and usr_selection < 8:
        print ( str(usr_selection) + ") " + a_line[usr_selection] )
    else:
        print ( str(usr_selection) + ") " + "Not a permitted number" )
except ValueError:
    print ("Invalid data entry detected. \nPlease try again.")
