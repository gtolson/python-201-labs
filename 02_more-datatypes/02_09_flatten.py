# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
starter_list2 = [[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]

#flattened_list = [item for sl in starter_list for item in sl]
flattened_list = []
for sl in starter_list:
    if isinstance(sl, list):
        for item in sl:
            flattened_list.append(item)
print(flattened_list)


# flatten nested lists using Iterable base python lib 
from typing import Iterable 

def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
print(list(flatten(starter_list2)))


# flattlen nested list using pip installed iteration_utilities
from iteration_utilities import deepflatten
print(list(deepflatten(starter_list2)))