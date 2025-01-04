# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

add_nums = lambda *args: sum(args)

result = add_nums(9,9,9)

print(result)
