# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')


fish_list2 = [f for f in fish_tuple if "fish" in f[-4:]]
print(fish_list2)

