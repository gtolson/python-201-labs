# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

user_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  min_num = int()
  max_num = int()
  tot_num = 0
  avg_num = int()
  for num in num_list:
    if not min_num:
      min_num = num
    elif num <= min_num:
      min_num = num
  for num in num_list:
    if not max_num:
      max_num = num
    elif num >= max_num:
      max_num = num
  for tnum in num_list:
    tot_num = tot_num + tnum
  avg_num = tot_num / len(num_list)
  dict_output = {'min_number':min_num,'max_number':max_num,'total_num':tot_num,'average_num':avg_num}
  return dict_output

# call the function below here
print(stats(user_list))