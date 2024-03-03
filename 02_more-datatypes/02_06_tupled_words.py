# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


#user_str = input("Please enter a sentence: ")
user_str = "My dog has flees"
result_list = []

usr_str_list = user_str.split()
print(usr_str_list)

for word in usr_str_list:
    wordlist = []
    for letter in word:
        wordlist.append(letter)
    wordlist_tup = tuple(wordlist)
    result_list.append(wordlist_tup)

    
print(result_list)
    