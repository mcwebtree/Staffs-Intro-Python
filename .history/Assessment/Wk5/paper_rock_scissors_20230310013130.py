# play Rock Paper Scissors - best of 3

# imports
import random as r

#helpers

def get_play():
    s_err=""
    while True:
        try:
            p_play=input( f"{s_err}Please enter your selection ([R]ock/[P]aper/[S]cissors): ").upper()
            if p_play in ['R','P','S']:
                break
            else :
                s_err = "Invalid selection: "
        except:
            s_err = "Invalid selection: "

    return p_play

## inits 
d_hands={ "R": {"Name": "Rock", "R": 0, "P": -1, "S": 1 },
          "P": {"Name": "Paper", "R": 1, "P": 0, "S": -1 },
          "S": {"Name": "Scissors", "R": -1, "P": 1, "S": 0 },
          }
l_choices = ['R', 'P', 'S']

player_score = int( 0 )
computer_score = int( 0 )

print ( "Welcome to Rock, Paper, Scissors " )
print ( "-" * 35 )
print ( f'{"Player":10} {"Computer":10} ')
while (player_score < 3 and computer_score > -3):
    p_play = get_play()
    p_play_name = d_hands[p_play]['Name']
    c_play = r.choice(l_choices)
    c_play_name = d_hands[c_play]['Name']
    print ( f'{p_play_name:10} {c_play_name:10}')
    res = d_hands[p_play][c_play]
    if res > 0:
        player_score = player_score + res
    elif res < 0: 
        computer_score = computer_score + res



