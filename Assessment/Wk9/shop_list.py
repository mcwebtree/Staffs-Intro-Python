# order a shopping list by price descending


# Screen control params
CLEAR = '\x1b[2K'
RESET = '\033[2J'
BLINKON = '\033[32;5m'
BLINKOFF = '\033[0m'
REVON = "\033[7m"
REVOFF = "\033[0m"
BLUEON = "\033[34m" # Blue text.
REDON= "\033[31m" #	Red text.
GREENON = "\033[32m" # 	Green text.
COLOUROFF = "\033[0m"	#Reset special formatting (such as colour).

def get_item():
    s_item=input(f"Please enter item {len(d_items)+1}: ")
    if s_item != "":
        try: 
            f_price=float(input(f"Please enter the {s_item} price: "))
        except: 
            # Error occured! 
            s_item=""
            f_price="0"

        if s_item != "":
            return s_item, f_price
    return "",0    

#inits
d_items={} # {'iteam 1': 1.99, 'item 2': 40.0, 'item 3': 20.0, 'item 4': 99.0, 'item 5': 404.0, 'item 6': 3.45}
s_item="Z"

print (RESET)
print (REVON + "Shopping List Sorter II   " + REVOFF)
print (" - bringing order to chaos")
print (BLUEON + "--------------------------" + COLOUROFF)

print ( f"Please enter 5 items and their prices. ")
print (BLUEON + "--------------------------" + COLOUROFF)
print ( f" *** {REDON}Press <enter> on blank item to exit list entry{COLOUROFF} ***\n")
while s_item > "":
    s_item, f_price = get_item()
    if s_item=="": 
        break
    
    d_items[s_item]=f_price

if len(d_items) > 0:
    l_items_sorted=sorted(d_items.items(), key=lambda item: item[1], reverse=True)

    i_max_len=max([len(key) for key in d_items.keys()])
    i_max_len = int(i_max_len)+2

    print ( "Your Shopping List: ")
    print (f'{"Item":{i_max_len}}  {"Price":>7}' )
    print ( "=" * (i_max_len+9))
    for t_item in l_items_sorted:
        print (f'{t_item[0]:{i_max_len}} £{t_item[1]:>7.2f}' )
