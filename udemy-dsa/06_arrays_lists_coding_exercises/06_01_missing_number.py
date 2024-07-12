# coding exercise 1: 

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

print(missing_number([1, 2, 3, 4, 6], 6))

# pairs- two sum: ;eetcode #1
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

# check if element exist in array
import numpy as np
def find(array, value):
    if type(array) == np.ndarray and array.size > 1:
      for i in range(len(array)):
          if array[i] == value:
              print(f'element {value} found at index: {i}')
              return
      print(f'element {value} not found in array')
    else:  
      print(f'first argument is not a np.array')
find(np.array([1,2,3]), 3)
find(np.array([1,2,3]), -3)
find(np.array([1,2,3]), None)
find(np.array(None), None)
