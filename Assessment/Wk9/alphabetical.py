# Sort 5 strings alphabetically.

# inits
a_string=[]

def print_me(lst1):
    for i in range(len(lst1)):
        print ( f'{i+1}: {lst1[i]}')
    print ("")
    
# get user input 
for i in range(5):
    tmp_var = input ( f"Please enter string {i+1}: " )
    if tmp_var.strip() == "":
        break
    a_string.append(tmp_var)

if len(a_string)==5:
    print ( f'Initial list is: ')
    print_me( a_string )

    a_string.sort()
    print ( f'Sorted list is: ')
    print_me( a_string )

    a_string_words = [' '.join(sorted(str.split(" "))).strip() for str in a_string]
    a_string_words.sort()
    print ( f'Internally Sensibly Sorted list is: ')
    print_me(a_string_words)

    a_string_chars = [(''.join(sorted([*str]))).strip() for str in a_string]
    a_string_chars.sort()
    print ( f'Internally Unsensibly Sorted Stripped list is: ')
    print_me(a_string_chars)
