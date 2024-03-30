# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    greeting = (f'Hello {name}! \n\n')
    goodby = (f'Thank you for taking the time to read this {name}! \n')
    body = (f'{text} \n\n')
    letter = greeting + body + goodby
    return letter

print(write_letter("Gary", "I hope this finds you well,\n\nI am giving you 100000$ because you are awesome! Please refer to the attached documnets for further details."))