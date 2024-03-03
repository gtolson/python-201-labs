# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

num_done = ''
userlist = []

print(f"The largest number is: {max(randlist)}")
print(f"The sum of all the numbers is: {sum(randlist)}")

#while num_done != 'e':
#    user_entry = (input("Please enter a number: "))
#    if user_entry.isalpha() or user_entry == '':
#        print("Please only enter numbers... ")
#        continue
#    user_entry = int(user_entry)
#    userlist.append(user_entry)
#    num_complete = input("Press any key to enter another number or press E to exit: ")
#    num_done = num_complete.lower()
#
#
#print(f"The largest number is: {max(userlist)}")
#print(f"The sum of all the numbers is: {sum(userlist)}")
    