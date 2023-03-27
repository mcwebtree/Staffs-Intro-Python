# Identify Thunderbirds. 

#inits
a_tbirds=['List of Thunderbird Pilots',
          'Thunderbird 1 pilot is Scott Tracy',
          'Thunderbird 2 pilot is Virgil Tracy',
          'Thunderbird 3 pilot is Alan Tracy',
          'Thunderbird 4 pilot is Gordon Tracy']
s_else='Have you never watched Thunderbirds!'
s_error = "Invalid entry. Please ensure you've entered a number!"

# header
print ( 'Thunderbirds Are Go' )
print ( '-' * 19)

# get input
i_val="A"
while i_val == "A":
    try: 
        i_val=int( input( "Please enter a number between 1 and 4 inclusive: "))

    except ValueError:  ## Value Error
        print ( "VE: " + s_error ) 
        i_val="A"
    except: ## General Error
        print ( "GE: " + s_error ) 
        i_val="A"

if i_val > 0 and i_val < 5:
    print ( a_tbirds[i_val])
else:
    print ( s_else )
    