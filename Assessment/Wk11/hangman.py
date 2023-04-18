

# params
api_ninjsas_key = "NZ7cUijXf6uoivDW6yl/EA==ufxyi04CTS0N25V6"
i_lives = 6
i_lives_remaining = i_lives
s_blank = "-"
i_sep_len = 50

# Variables
a_guesses=[]
a_letters=[]

import requests
import json 
import sys
import os
import time

sys.path.append(os.path.abspath('..\\inc\\'))

import screen as s
import helpers as h

def get_word():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': api_ninjsas_key})
    if response.status_code == requests.codes.ok:
        a_ret = json.loads(response.text)
        return a_ret['word'].upper()
    else:
        print("Error:", response.status_code, response.text)
        return ""
    
def remove_dups(x):
  return list(dict.fromkeys(x))

def show_grid():
    print ( s.RESET )
    print ( "Hangman Beta v0.1  ")
    print ( "Words courtesy of api-ninjas.com Random Words API")
    print ( "=" * i_sep_len)
    print ( "" )
    print ( f"Lives Remaining: {i_lives_remaining}/{i_lives} --> [ ", s.GREENON, "0" * (i_lives_remaining), s.REDON, "X" * (i_lives-i_lives_remaining), s.COLOUROFF, "]")
    print ( "" )
    print ( f"The word has {i_len} characters")
    print ( "" )
    print ( "=" * i_sep_len)
    print ( "" )
    print ( "The Word:     ", end ="" )
    for i in range(i_len):
        if s_word[i] in a_guesses:
            print ( s_word[i], end = "" )
        else:
            print ( s_blank , end = "" )
    print ( "" )
    print ( "" )
    print ( "=" * i_sep_len)
    print ( "" )
    print ( "Your Guesses: ", end ="" )
    print (", ".join(a_guesses) )
    print ( "" )
    print ( "=" * i_sep_len)
    print ( "" )

def check_won():
    f_win = True
    for val in a_letters:
        if val not in a_guesses:
            f_win = False
            break

    return f_win

def exit_print():
    print ( "Please play again soon " )
    print ( "" )
    print ( "The word was: " + s_word)
    print ( "" )


s_word = get_word()
if s_word != "":
    #print ( f"The word is '{s_word}'" )
    i_len = len(s_word)
    a_letters = remove_dups([*s_word])
    a_letters.sort()
    print (a_letters)
    show_grid()

    while check_won()==False:
        s_guess = input ( "Please enter a letter (type EXIT to quit): ").upper()
        if s_guess == "EXIT":
            exit_print()
            break

        # make sure it's only one character.
        s_guess=s_guess[0]

        if s_guess in a_guesses: 
            print ( "You've already guessed that!" )

        elif s_guess in a_letters:
            print ( "Yey, you've guessed correctly ")
            a_guesses.append(s_guess)
            a_guesses.sort()

        else:
            print ( "Oh No, that's not in the word")
            a_guesses.append(s_guess)
            a_guesses.sort()

            i_lives_remaining -= 1
            if i_lives_remaining < 1:
                print ( "All lives lost! :( " )
                exit_print()
                break
        
        time.sleep(1)
        show_grid()

    if check_won():
        print ( "*" * i_sep_len )
        print ( f"{'Congratulations':^{i_sep_len}}")
        print ( "*" * i_sep_len )
        print ( "" )

        