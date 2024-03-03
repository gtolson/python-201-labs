# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. Convert to a different data type
list_set = set(list_)
print(list_set)


# 2. Use a loop and a second list to solve it more manually
list_dedup = []
for item in list_:
    if item not in list_dedup:
        list_dedup.append(item)
print(list_dedup)