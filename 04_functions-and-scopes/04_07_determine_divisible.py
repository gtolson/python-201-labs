# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


user_num_str = input("Please enter a number between 1 and 1,000,000: ")
user_int = int(user_num_str)

def four_or_seven(user_int):
    if user_int % 4 == 0 or user_int % 7 == 0:
        for_or_sev_out = True
    else:
        for_or_sev_out = False
    return for_or_sev_out

def four_and_seven(user_int):
    if user_int % 4 == 0 and user_int % 7 == 0:
        for_and_sev_out = True
    else:
        for_and_sev_out = False
    return for_and_sev_out

#
print(f"Is the number {user_int} divisible by 4 OR 7? : {four_or_seven(user_int)}")
print(f"Is the number {user_int} divisible by 4 AND 7? : {four_and_seven(user_int)}")