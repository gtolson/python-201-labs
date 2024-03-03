#!/usr/bin/python

####################
#Write a script that takes a sentence from the user and returns:
#
#    the number of lower case letters
#    the number of uppercase letters
#    the number of punctuations characters
#    the total number of characters
#
#Use a dictionary to store the count of each of the above.
#
#Note: ignore all spaces.
####################

import string

user_input = input("Please enter a full sentance here...: ")

ui_list = list(user_input)

counts = {"lower_case": 0, "upper_case": 0, "punctuation": 0, "total": 0}

for char in ui_list:
    if char != " ":
        counts["total"] += 1
    if char.islower():
        counts["lower_case"] += 1
    if char.isupper():
        counts["upper_case"] += 1
    if char in string.punctuation:
        counts["punctuation"] += 1


for key, value in counts.items():
    print(f"{key.capitalize()} char count is: {value}")
