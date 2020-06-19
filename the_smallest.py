smallest = None
print("before")
for value in [25, 34, 56, 13, 43, 9, 54, 3] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)

print("after", smallest)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)