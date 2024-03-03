# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


#userlist = [1,2,3,4,5,6,7,8,9,10]

userlist = []
num_done = ""

while num_done != 'e':
    user_entry = (input("Please enter a number: "))
    if user_entry.isalpha() or user_entry == '':
        print("Please only enter numbers... ")
        continue
    user_entry = int(user_entry)
    userlist.append(user_entry)
    num_complete = input("Press any key to enter another number or press E to exit: ")
    num_done = num_complete.lower()

print(str(userlist)[1:-1].replace(" ", ""))

userlist_even = userlist[1::2]
#print(str(userlist_even)[1:-1].replace(" ", ""))

userlist_odd_rev = userlist[-2::-2]
#print(str(userlist_odd_rev)[1:-1].replace(" ", ""))

userlist_combine = userlist_even + userlist_odd_rev
print(str(userlist_combine)[1:-1].replace(" ", ""))