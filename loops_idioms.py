#COUNTING IN A LOOP : to count how many times we excecuted a loop, we introduce a
# count variable that starts at 0ans we add one to it, each time through the loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15, 67] :
    zork = zork + 1
    print(zork, thing)
print("After", zork)

#SUMMING IN A LOOP : to add up a value we encaunter in a loop, we introsuce a sum variable
#that stars at 0 and we add the value to the sumeach time through te loop.

zeed = 0
print("Before", zeed)
for thing in [9, 41, 12, 3, 74, 15, 67, 27, 29, 56] :
    zeed = zeed + thing
    print(zeed, thing)
print("After", zeed)

#FINDING a AVERANGE
count = 0
sum = 0
print("Before",count, sum)
for value in [9, 41, 12, 3, 74, 15, 67, 27, 29, 56] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum /count)

#SEARCH WITH BOOLEAN VARIABLE : If we want to know if a value was found,
# we use a variable that starts at FALSE and it is set to TRUE
#as soon as we find what we are looking for.
found = False
print("before", found)
for value in [9, 41, 12, 67, 3, 77, 28] :
    if value == 3 :
        found = True
        break
    print(found, value)
print("after", found)
