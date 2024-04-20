def titlecase(text):
    titlecase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return " ".join(titlecase)


user_in = ""
while user_in.lower() != 'exit':
    user_in = input("Please enter a headline, or type 'exit' to quit: ")
    print(titlecase(user_in))