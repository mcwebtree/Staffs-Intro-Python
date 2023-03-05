
# #// this will work as its replacing the entire contents. 
# my_song = "All Too Wall"
# print ( my_song )
# my_song = 'All Too Well'
# print ( my_song )

# #// this will crash as I can't change PART of 
# # (comment this out to test the next part)
# # my_song[6] = 'e'
# # print ( my_song )
    
# # this all works. because each is a replacement
# my_list = ["bob",1,2.3,"steve"]
# print ( my_list )
# my_list[3]=12.23
# print ( my_list )
# my_list[3]=my_list[3]*5 # this doesn't amend the value, it replaces it with a new one. 
# print ( my_list )

# # this will work as the entire string part of the list can be replaced. 
# my_list[0]="flip"
# print ( my_list )

# # this will crash because the string part cannot be manipulated inside itself
# # my_list[0][2]="o"
# # print ( my_list )

lst = []

n = int(input("Enter number of employees"))
#a = 0
for a in range(0, n):
    name = input("Enter name of employees")
    lst.append(name)
    #a=a+1
    
print(lst)
