# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.


user_str = input("Please enter a sentence: ")

usr_str_list = user_str.split()

new_list = []
dup_list = []
dup_dict = {}

for n in usr_str_list:
    if n not in new_list:
        new_list.append(n)
    else:
        dup_dict[n] = usr_str_list.count(n)

max_item = max(dup_dict, key=dup_dict.get)

print(f"The word \"{max_item}\" appears {dup_dict[max_item]} times.")