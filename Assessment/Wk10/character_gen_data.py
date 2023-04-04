# read data from json file

# imports
import json


# definitions
REDON= "\033[31m" #	Red text.
GREENON = "\033[32m" # 	Green text.
COLOUROFF = "\033[0m"	#Reset special formatting (such as colour).

CLEAR = '\x1b[2K'
RESET = '\033[2J'


def show_char_stats():
    
    #print (RESET)

    print ( "-" * 80)
    print ( f"| {'Class':12}", end="|"  )
    for key in a_attributes:
        print ( f'{a_attributes[key]["Name"]:^12}', end="|"  )
    print ("")
    print ( "-" * 80)
    
    for key in a_characters:    
        print (a_posit[key], end="")
        print ( f' {key:12}', end="|"  )
        for this_key in a_characters[key]:
            print ( f'     {a_characters[key][this_key]:>2}     ', end="|"  )
        print ("")

    print ( "-" * 80)

a_attributes = {"S": {"Name": "Strength", "Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "I": {"Name": "Intelligence", "Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "W": {"Name": "Wisdom","Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "D": {"Name": "Dexterity","Min": 3, "Max": 18, "Initial": 0, "Current": 0},
                "C": {"Name": "Constitution","Min": 3, "Max": 18, "Initial": 0, "Current": 0}}

a_characters = { "Warrior": {"S": 0, "I": 0, "W": 0, "D": 0, "C": 0}, 
                "Wizard": {"S": 0, "I": 0, "W": 0, "D": 0, "C": 0}, 
                "Thief": {"S": 0, "I": 0, "W": 0, "D": 0, "C": 0},
                "Necromancer": {"S": 0, "I": 0, "W": 0, "D": 0, "C": 0}}

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


print ("Importing data from JSON")
print ("------------------------")


# Opening JSON file
with open('char_classes.json') as json_file:
    d_json_data=json.load(json_file)
#print(d_json_data)

for char in d_json_data:
    s_role=char.capitalize()
    for k, v in d_json_data[char].items():
        s_attr=k[0].upper()
        if v == '-':
            v = 0
        
        a_characters[s_role][s_attr]=int(v)

print ("Character requirements are:")
show_char_stats()

