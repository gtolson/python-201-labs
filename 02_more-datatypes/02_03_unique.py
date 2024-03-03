# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
counter = 1
counter = int(counter)
unique_list_ = []
bad_list_ = []


for n in list_:
   # print(counter)
    if n not in list_[counter:] and n not in bad_list_:
        unique_list_.append(n)
    else:
        bad_list_.append(n)
    counter += 1

print(unique_list_)