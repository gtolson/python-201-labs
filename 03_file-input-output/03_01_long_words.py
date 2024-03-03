# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

f = open('words.txt', 'r')

txt_file = f.read()
txt_file2 = txt_file.split()

for word in txt_file2:
    if len(word) > 20:
        print(word)

f.close()