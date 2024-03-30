# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def greet(greeting: str, name: str) -> str:
    greetings = ""
    sentence = f"{greeting}, {name}! Hope this finds you well!"
    greetings += sentence + "\n\n"
    return greetings

def write_letter(name,greeting,text):
    greeting = greet(greeting,name)
    goodby = (f'Thank you for taking the time to read this {name}! \n')
    body = (f'{text} \n\n')
    letter = greeting + body + goodby
    return letter

print(write_letter("Gary","Hello", "I am giving you 100000$ because you are awesome! Please refer to the attached documnets for further details."))