# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

f = open('words.txt', 'r')
maxnum = 0
minnum = 1000
txt_file = f.read()
txt_file_list = txt_file.split()
txt_file_list_tup = []
max_number_out = []
shortest_number_out = []

for w in txt_file_list:
    wlen = len(w)
    txt_file_list_tup.append((w,wlen))
    
# Find the largest number
for letlgnum in txt_file_list_tup:
    lln = letlgnum[1]
    if lln > maxnum:
        maxnum = lln

# Find the smallest number
for letsnum in txt_file_list_tup:
    lsn = letsnum[1]
    if lsn < minnum:
        minnum = lsn

# Get the largest words and print them
[max_number_out.append(x[0]) for x in txt_file_list_tup if x[1] == maxnum ]

print(f"\nThese words are the longest with a count of {maxnum}")
for mno in max_number_out: 
    print(mno)

# Get the shortest words and print them
[shortest_number_out.append(y[0]) for y in txt_file_list_tup if y[1] == minnum ]

print(f"\n\nThese words are the shortest with a count of {minnum}")
for sno in shortest_number_out: 
    print(sno)

# Get the total number of words in the file
number_of_words = len(txt_file_list)
print(f"The number of words in this file: {number_of_words}")

f.close()