# somthing to do with a restaurant based on existing code. 

print("Main dishes are:")
print("1. Lasagne")
print("2. Stir Fry")
main_dish = int(input("Please select dish: "))

if main_dish == 1:
    print("Side dishes are:")
    print("1. Garlic bread")
    print("2. Fries")
    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Lasagne with garlic bread")
    elif side_dish == 2:
        print("You have selected Lasagne with fries")
    else:
        print("Invalid item selected")
elif main_dish == 2:
    print("Side dishes are:")
    print("1. Noodles")
    print("2. Crispy Seaweed")
    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Lasagne with garlic bread")
    elif side_dish == 2:
        print("You have selected Lasagne with fries")
    else:
        print("Invalid item selected")
else:
    print("Invalid item selected")