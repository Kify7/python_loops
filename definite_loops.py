for i in [5, 4, 3, 2, 1] :
    print(i)
print("Blastoff!")

friends = ["Argelia", "Mariana", "Taya", "Isa", "Claus", "Ceci"]
for friend in friends :
    print("Happy New Year", friend)
print("Done!")

#FINDING THE LARGEST VALUE

#1) Set some variables to initial values
#2) for thing in data: Look foe somthing or do somethinh to eachentry sepatatlyupdating a variable
#3) Look at the variables

#looping for  a set
print("before")
for thing in [9, 41, 12, 3, 74, 15, 67] :
    print(thing)
print("after")


largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15, 67] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
    
print("After", largest_so_far)