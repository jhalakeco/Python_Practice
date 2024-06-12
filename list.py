# List in pyhton

friends = ["Rolf", "Bob", "Anne"] # this is list in Python and this is a list of three strings
type(friends) # checking the object class

# now in order to extract only single value from the list
print(friends[0]) # here i am calling the first value and it starts from 0
# we can also put character an numerica/ integer objects inside this list. However, the best practice is to keep all the necessay identical objects into a single list.

# to find the length of the object
print(len(friends))

# List inside list
uncles = [
    ["Maddie", 45],
    ["Rodger", 43],
    ["Peter", 54]
] # anything is borered by square bracket [] is consodered list. So it is a list inside the list

print(len(uncles))
print(uncles[0][1]) # this means, the second element from the first list is being accessed

# adding element to a list
friends.append("Tim") # .append function enables adding element in an existing list
print(friends)

# removing element from a list
friends.remove("Tim") # .remove function enables removing an element from the list
print(friends)

# Removing element from multiple element list
uncles.remove(["Peter", 54]) # we must type the exact element as stated in the list
print(uncles)