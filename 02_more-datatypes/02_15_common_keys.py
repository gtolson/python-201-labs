# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}

for x1, y1 in dict_1.items():
    #print(x1, y1)
    if x1 in dict_2:
        dict_3[x1] = dict_2[x1] + y1
    if x1 not in dict_2:
        dict_3[x1] = y1
for x2, y2 in dict_2.items():
    if x2 not in dict_1:
        dict_3[x2] = y2

sorted_dict_3 = dict(sorted(dict_3.items()))
print(sorted_dict_3)

