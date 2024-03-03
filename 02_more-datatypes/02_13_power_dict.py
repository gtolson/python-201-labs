# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}


dict1 = {}

for x in range(10):
    y = str(x)
    dict1[y] = x * x
    
print(dict1)