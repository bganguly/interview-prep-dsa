# coding exercise 1:

import numbers
import numpy as np

# question 1
# missing number
# Write a function to find the missing number in a given integer array of 1 to 100.
# Example
# missing_number([1, 2, 3, 4, 6], 6) # 5
# arr of natural numbers potentially sorted
# n is one more than the number of elemnts in arr
def missing_number(arr, n):
    sum_of_n_numbers = n * (n+1)/2
    sum_of_elements_in_arr = sum(arr)
    return sum_of_n_numbers - sum_of_elements_in_arr

print(f"Missing number is: {missing_number([1, 2, 3, 4, 6], 6)}")

# question 2
# pairs- two sum: leetcode #1
# find indices of numbers (in an array) that add to a target number
# Write a function to find the indices of elements whose sum add to a given array.
# Example
# two_sum([1, 2, 3, 4, 6], 5) # (1,,4)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

nums = [2, 7, 11, 15]
target = 26
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")
print()

# question 3
# check if element exist in array
def find(array, value):
  """ Returns a tuple is_error, input_is_not_array, value_is_not_number, value_found, index_found """
  if type(array) == np.ndarray and array.size > 1:
    if isinstance(value, numbers.Number):
      for i, num in enumerate(array):
          if num == value:
              return False, False, False, value, i
      return True, False, False, value, None
    else:
      return True, False, True, value, None
  else:
    if isinstance(value, numbers.Number):
      return True, True, False, value, None
    else:
      return True, True, True, value, None

def find_helper(result):
  if result[0] == False:
    print(f'value {result[3]} found at index: {result[4]}')
  else:
    if result[1] == False:
      if result[2] == False:
        print(f'value {result[3]} not found in array')
      else:
        print(f'value {result[3]} is not numeric')
    else:
      if result[2] == False:
        print('input array is not a np.array')
      else:
        print('input array is not a np.array and value is also not numeric')

result = find(np.array([1, 2, 3]), 3)
find_helper(result)
result = find(np.array([1, 2, 3]), -3)
find_helper(result)
result = find(np.array([1, 2, 3]), None)
find_helper(result)
result = find(np.array(None), None)
find_helper(result)
