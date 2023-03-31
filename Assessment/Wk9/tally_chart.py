# Do some voting and the like.

import os
import sys
import time
import random as r
import matplotlib.pyplot as mpl

sys.path.append(os.path.abspath('..\\inc\\'))

import screen as s

names = [  "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",  "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",  "Michael", "Abigail", "Ethan", "Emily", "Daniel", "Elizabeth", "Matthew", "Mila", "Jackson", "Ella",  "Sebastian", "Avery", "Aiden", "Sofia", "Logan", "Camila", "Mason", "Aria", "Ezra", "Scarlett",  "Grayson", "Victoria", "Carter", "Madison", "Luke", "Luna", "Jayden", "Grace", "Levi", "Chloe",  "Isaac", "Penelope", "Lincoln", "Riley", "Nicholas", "Zoey", "David", "Lily", "Connor", "Ellie",  "Wyatt", "Nora", "Owen", "Hazel", "Caleb", "Aurora", "Ryan", "Addison", "Gabriel", "Hannah",  "Nathan", "Stella", "Leah", "Maya", "Isaiah", "Aaliyah", "Eli", "Nova", "Hunter", "Eleanor",  "Landon", "Paisley", "Nicholas", "Naomi", "Jeremiah", "Ariana", "Ezekiel", "Claire", "Aaron", "Elena"]

a_candidates={}
a_results={}

def init_candidates():
    global a_candidates
    l_names=r.sample(names,5)
    for name in l_names:
        a_candidates[name]=0


def get_vote():
    global a_candidates

    l_candidates=list(a_candidates.keys())
    r.shuffle(l_candidates)
    display_candidates(l_candidates)
    try:
        i_vote=int ( input ("Please enter the number of your chosen candidate [-1 to quit]: ") )
        if i_vote == -1:
            return -1
        elif 1 <= i_vote <= len(l_candidates):
            a_candidates[l_candidates[i_vote-1]] += 1
            return 1
        else:
            print ( "Invalid vote cast" )
            time.sleep(1)
            return 0
    except:
        print ( "Invalid vote cast" )
        time.sleep(1)
        return 0

def print_results():
    global a_results
    # l_results= [('Harper', 8), ('Owen', 7), ('Aaliyah', 5), ('Connor', 4), ('Aaron', 1)]
    l_results=sorted(a_candidates.items(), key=lambda cand: cand[1], reverse=True)
    #print ( l_results )
    a_results=dict(l_results)
    #print ( a_results )

    print ( s.RESET )
    
    print ("The voting results are:")
    for cand in l_results:
        print ( f'{cand[0]:10} {cand[1]:>3}')

def display_candidates(l_cand):
    # clear the screen
    print (s.RESET)

    print ("Your Candidates:")
    for i in range(len(l_cand)):
        print ( f'{i+1}) {l_cand[i]} ')

def create_pie():
    # create a pie chart
    mpl.pie(a_results.values(), labels=a_results.keys() ,  autopct='%1.1f%%')
    # add a title
    mpl.title('Talent Contest Votes')
    # create a legend
    legend_labels = [f"{k} ({v})" for k, v in a_results.items()]
    mpl.legend(legend_labels, title="Candidates", loc="lower right", bbox_to_anchor=(1, 0, 0.5, 1))
    mpl.subplots_adjust(right=0.7)

    # show the plot
    mpl.show()

# actually do something. 

init_candidates()
while True:
    ret = get_vote() 
    if ret == -1:
        break

print_results()

f_pie = input("Do you want a pie chart of the results [Y/N]? ").upper()
if f_pie == "Y":
    create_pie()