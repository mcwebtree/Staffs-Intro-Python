# Character Generator

# imports
import random as r
import time 

# definitions
REDON= "\033[31m" #	Red text.
GREENON = "\033[32m" # 	Green text.
COLOUROFF = "\033[0m"	#Reset special formatting (such as colour).

CLEAR = '\x1b[2K'
RESET = '\033[2J'

## function to get an integer with error checking
def get_int(input_prompt, min_val=int(1), max_val=int(100)):
    return_value=int(0)
    int_val=int(-1)

    while not ((int_val >= min_val and int_val <= max_val)) and not int_val == 0 :
        try:
            get_val=input(input_prompt + f" (Min: {str(min_val)} Max: {str(max_val)} Exit: 0) : ")
            int_val=int(get_val)

            ## exit if select 0
            if  int_val==0: 
                break
        
            return_value=int_val
        except:
            print ( f"Invalid '{input_prompt}' value entered '" + get_val + "'" ) 
            
    return return_value

def show_stats(s_class = ""):
    
    print (RESET)

    print ( 'Your skills and the requirements: ')
    print ( "-" * 80)
    print ( f"| {'Class':12}", end="|"  )
    for key in a_attributes:
        print ( f'{a_attributes[key]["Name"]:^12}', end="|"  )
    print ("")
    print ( "-" * 80)
    # print initial scores
    if s_class != "":
        print ( f"| {'Initial':12}", end="|"  )
        for key in a_attributes:
            print ( f'     {a_attributes[key]["Initial"]:>2}     ', end="|"  )
        print ("")

    # print Current scores
    print ( f"| {'Your score':12}", end="|"  )
    for key in a_attributes:
        if s_class!="":
            if required_skill_points(s_class, key) == 0:
                print ( GREENON, end="")
        print ( f'   {float(a_attributes[key]["Current"]):^6.1f}   '+ COLOUROFF, end="|"  )
    print ("")
    print ( "-" * 80)
    # if a class is chosen then output the required stats. 
    if s_class != "":
        print ( f"| {'Required':12}", end="|"  )
        for key in a_attributes:
            rsp=int(required_skill_points(s_class,key))
            if rsp>0 :
                print ( f'     {rsp:>2}     ', end="|"  )
            else:
                print ( f'            ', end="|"  )
        print ("")
        
        print ( f"| {'Free':12}", end="|"  )
        for key in a_attributes:
            fsp=int(free_skill_points(s_class,key))
            if fsp > 0 :
                print ( f'     {fsp:>2}     ', end="|"  )
            else:
                print ( f'            ', end="|"  )

        print ("")

        print ( "-" * 80)
    
    for key in a_characters:
        if s_class=="" or s_class==key:
            print (a_posit[key], end="")
            if check_stats(key)== True:
                print ( GREENON, end="" )
            print ( f' {key:12}'+COLOUROFF, end="|"  )
            for this_key in a_characters[key]:
                if a_characters[key][this_key]>a_attributes[this_key]["Current"]:
                    print (REDON, end="")
                else:
                    print (GREENON, end="")
                print ( f'     {a_characters[key][this_key]:>2}     '+ COLOUROFF, end="|"  )
            print ("")

    print ( "-" * 80)

def randomise_attributes():
    global a_attributes
    for key in a_attributes:
        a_attributes[key]["Initial"]=r.randrange(a_attributes[key]["Min"], a_attributes[key]["Max"]+1)
        a_attributes[key]["Current"]= a_attributes[key]["Initial"]

def check_stats(s_class):
    f_valid=True
    for s_stat in a_characters[s_class]:
        if a_characters[s_class][s_stat]> a_attributes[s_stat]["Current"]:
            f_valid=False
    return f_valid

# list the categories with free points
def list_excess_categories(s_class):
    l_available=[]
    for key in a_characters[s_class]:
        if free_skill_points(s_class, key) > 0:
            l_available.append(key)
    return l_available

# list the categories requiring points
def list_reqd_categories(s_class):
    l_reqd=[]
    for key in a_characters[s_class]:
        if required_skill_points(s_class,key) > 0:
            l_reqd.append(key)
    return l_reqd

# look how many points are available across all skills. 
def free_points(s_class):
    i_points=0
    for key in a_characters[s_class]:
        i_points += free_skill_points(s_class,key)
    return i_points

# Look how many points are available in a given skill
def free_skill_points(s_class, s_skill):
    i_points=0
    i_min_allowed = a_attributes[s_skill]["Min"]
    i_min_test = a_characters[s_class][s_skill]
    # check it maintains the minimum required points. 
    if i_min_test<i_min_allowed:
        i_min_test=i_min_allowed
    ## see what's free
    if  (a_attributes[s_skill]["Current"])>i_min_test:
        i_points = (a_attributes[s_skill]["Current"])-i_min_test
    return i_points

def required_points(s_class):
    i_points=0
    for key in a_characters[s_class]:
        i_points += required_skill_points(s_class, key)
    return i_points    

def required_skill_points(s_class, s_skill):
    i_points=0
    if a_attributes[s_skill]["Current"]<a_characters[s_class][s_skill]:
        i_points = a_characters[s_class][s_skill]-a_attributes[s_skill]["Current"]
    return i_points   

def move_points(s_class):
    l_skills = list_excess_categories(s_class)
    s_source="X"
    while not s_source in l_skills and s_source != "Q":
        s_source=input(f'Please enter the source ability ({",".join(l_skills)}) [Q to Exit]:').upper()
    
    if s_source != "Q":
        i_free_p = free_skill_points(s_class, s_source)

        if i_free_p == 0 :
            print ("You don't have any free points on that skill")
        else :
            l_skills = list_reqd_categories(s_class)
            s_target="X"
            while not s_target in l_skills:
                s_target=input(f'Please enter the target ability ({",".join(l_skills)}) :').upper()

            i_req_p = required_skill_points(s_class, s_target)

            print (f"You have {i_free_p} available ({i_free_p/2}) and require {i_req_p}. (2 free points =  1 required points).")
            i_move=-1
            while (i_move < 0 or i_move > i_free_p) :
                i_move = get_int("How many points do you want to move?",1,i_free_p)

            a_attributes[s_source]["Current"] -= i_move
            a_attributes[s_target]["Current"] += (i_move/2)
        return "1"
    else:
        return "Q"
    
a_attributes = {"S": {"Name": "Strength", "Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "I": {"Name": "Intelligence", "Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "W": {"Name": "Wisdom","Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "D": {"Name": "Dexterity","Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "C": {"Name": "Constitution","Min": 3, "Max": 18, "Initial": 0, "Current": 0}}

a_characters = { "Warrior": {"S": 15, "I": 0, "W": 0, "D": 12, "C": 10}, 
                "Wizard": {"S": 0, "I": 15, "W": 10, "D": 10, "C": 0}, 
                "Thief": {"S": 10, "I": 9, "W": 0, "D": 15, "C": 0},
                "Necromancer": {"S": 10, "I": 10, "W": 15, "D": 0, "C": 0}}

a_posit = { 
      "Warrior": "1", 
      "1": "Warrior",
      "Wizard": "2",  
      "2": "Wizard", 
      "Thief": "3",
      "3": "Thief",
      "Necromancer": "4",
      "4": "Necromancer"
      }

i_target = 0

randomise_attributes()
show_stats()

i_target=get_int("Please select your desired class :",1,4)

if i_target > 0:
    s_target = a_posit[str(i_target)]
    req_p = required_points(s_target)
    free_p = free_points(s_target)
    
    show_stats(s_target)
    print ( f"You require {req_p} extra points to become a {s_target}." )

    if int(req_p*2)>int(free_p):
        print ( f"You only have {free_p} free points, (and you need {req_p*2}). \nSadly that's not enough free points to become an {s_target}. \nPlease try again.")
    else :
        print ( f"You have {free_p} points available and you only need {req_p*2} free points!")
        
        while check_stats(s_target)==False:
            ret_val=move_points(s_target)
            if ret_val=="Q":
                break
            show_stats(s_target)

        if check_stats(s_target)==True:
            print ( f"Congratulations you're now a {s_target}!" )
         
        print ( f'Thanks for playing, please come back soon.')
    