# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

# - Convert the string shown below into a tuple.
string_tup = tuple(string)
print(f'"string_tup" = {type(string_tup)}')

# - Convert the tuple into a list.
string_list = list(string_tup)
print(f'"string_list" = {type(string_list)}')

# - Change the `c` character in your list into a `k`
new_string_list = ['k' if lett == 'c' else lett for lett in string_list ]
string_list = new_string_list
print(string_list)


# - Convert the list back into a tuple.
string_list= tuple(string_list)
print(f'"string_list" = {type(string_list)}')


# - Change the `c` character in the string into a `k` BONUS
tmp_string = ""
new_string = ""

for letter in string:
    if letter == 'c':
        tmp_string = new_string + 'k'
        new_string = tmp_string
    else:
        tmp_string = new_string + letter
        new_string = tmp_string
print(new_string)



