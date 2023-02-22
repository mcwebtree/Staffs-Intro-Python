# Nothing for a Pair (not in this game)

# imports
import random

# inits
a_cards=["Card Values"]
a_cards.append("Ace")
for i in range(2,11): a_cards.append(i)
a_cards.append("Jack")
a_cards.append("Queen")
a_cards.append("King")

a_suite=["Card Suites"]
a_suite.append("Clubs")
a_suite.append("Diamonds")
a_suite.append("Hearts")
a_suite.append("Spades")

s_success="Congratulations! You're a Winner!"
s_failure="Better luck next time :("
s_invalid="Sorry your guess wasn't understood"

print ( "Higher or Lower - Come on Down " )
print ( "-" * 40)

# deal card
i_card = random.randint(1,13)
i_suite = random.randint(1,4)

print ( f'Your first card {i_card} is a {a_cards[i_card]} of {a_suite[i_suite]}')

your_guess = input("Please enter if you think the next card will be 'higher' or 'lower' :").lower()

print ( f'You guessed {your_guess} ')

# deal card
i_card_2 = random.randint(1,13)
i_suite_2 = random.randint(1,4)

print ( f'Your second card {i_card_2} is a {a_cards[i_card_2]} of {a_suite[i_suite_2]}')

if your_guess=="higher" :
    if i_card < i_card_2 :
        print ( s_success )
    else :
        print ( s_failure )
elif your_guess=="lower" :
    if i_card > i_card_2 :
        print ( s_success )
    else :
        print ( s_failure )
else :
        print ( s_invalid )
        print ( s_failure )
