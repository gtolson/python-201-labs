# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
for s in string:
    print(s)
print("===========")
string = tuple(string)
for s in string:
    print(s)
