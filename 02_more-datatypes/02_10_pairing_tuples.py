# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)
# Write your code below here


# Sort and make sure even number of items.
randlist.sort()
if len(randlist) % 2 != 0:
    randlist.append(int(0))

# Set vars
randlist_len = len(randlist)
start_index = 0
end_index = 2
tup_list = []

# Create the list of tuples
while end_index <= randlist_len:
    tup_list.append(tuple(randlist[start_index:end_index]))
    start_index += 2
    end_index += 2

# Print each tuple
for tup in tup_list:
    print(tup)



