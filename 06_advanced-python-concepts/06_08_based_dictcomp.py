# Write a dictionary comprehension that maps each integer
# between `0` and `999` to a list of the digits that represents
# that integer in base 10. That is, your output should be:
#
# {0: [0], 1: [1], 2: [2], 3: [3], ...,
# 10: [1, 0], 11: [1, 1], 12: [1, 2], ...,
# 999: [9, 9, 9]}
#
# CHALLENGE: Write another dictionary comprehension that works the same
# but for base 2 (binary)! The output values should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ...,
# 7: [1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], ...,
# 999: [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]}



dict_test = {}

for x in range(1000):
    dict_test[x] = []
    for y in str(x):
        dict_test[x].append(int(y))
#print(dict_test)
    

dict = { k: [ int(v) for v in str(k) ] for k in range(1000) }
print(dict)


dict2 = { k: [ int(v) for v in bin(k)[2:] ] for k in range(1000) }
print(dict2)
