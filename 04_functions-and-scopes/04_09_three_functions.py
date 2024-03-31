# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.



def name_entry():
    name_in = input("What is the name of the person you want to address?: ")
    return name_in

def greeting(name):
    name  = name_entry()
    full_greeting = (f"\nHi {name}, welcome to the Thunderdome, \n\n")
    return full_greeting

def body(greeting):
    greeting = greeting(name_entry)
    letter_so_far = ""
    main_body = (f'You have earned the right to compete in a battle of wills against the worlds greatest warriors. \n\n')
    letter_so_far = greeting + main_body
    return letter_so_far

def letter(body):
    close = (f'Best of luck to you brave warrior! \n')
    body = body(greeting)
    full_letter = body + close
    return full_letter


print(letter(body))
