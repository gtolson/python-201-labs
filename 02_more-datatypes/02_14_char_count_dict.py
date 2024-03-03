# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


user_input = input("Please enter a string: ")
result = {}

for let in user_input:
    x = user_input.count(let)
    result[let] = x
    
print(result)