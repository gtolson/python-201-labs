# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


#Open the words file and reverse the list
with open("words.txt", "r") as f:
    txt_file = f.read()
    word_list = txt_file.split()
    word_list.reverse()

# covert the list to a string using list comprehension
with open("words_reverse.txt", "w") as fw:
    word_list_str = '\n'.join(str(x) for x in word_list)
    fw.write(word_list_str)