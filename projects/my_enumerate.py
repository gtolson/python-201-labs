# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(items, start=None):  # add your arguments
    list_len = range(len(items))
    tup_list = []
    if start is None:
        start_int = 0
    else:
        start_int = start
    for i in list_len:
        ind = i + start_int
        tup_list.append((ind, items[i]))
    return tup_list

locations = ["spain", "india", "united states", "united kingdom", "mexico"]

# enumerate returns a list of tuples cotaining the index and the value.
for index, country in my_enumerate(locations, start=0):
    print(f"{index} : {country}")