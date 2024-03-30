# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(bread, *toppings):
    sandwich_contents = []
    sandwich_contents.append(bread)
    for topping in toppings:
       sandwich_contents.append(topping)
    sandwich_contents.append(bread)
    made_sandwich = ','.join(sandwich_contents)
    return made_sandwich
     
print(make_sandwich("Whole Wheat Bread", "Turkey", "Lettuce", "Tomato", "Onion", "Extra Pickle", "Dejon Mustard"))