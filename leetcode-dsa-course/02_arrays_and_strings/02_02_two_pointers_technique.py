from typing import List


def isPalindrome (input):
  left = 0
  right = len(input) - 1

  while left < right:
    if (input[left] != input[right]):
      return False
    left += 1
    right -= 1
    
  return True  


# print(isPalindrome('abaaba'))

def does_pairwise_sum_exist (nums, target):
  left = 0
  right = len(nums) - 1

  while left < right:
    curr = nums[left] + nums[right]
    if curr == target:
        return True
    if curr > target:
        right -= 1
    else:
        left += 1
    
  return False


# print(does_pairwise_sum_exist([1, 2, 4, 6, 8, 9, 14, 15], 13))

def combine_sorted_arrays(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans

# print(combine_sorted_arrays([1,4,7,20], [3,5,6]))

def isSubsequence(s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# print(isSubsequence("tig", "tiger"))

def reverseString(s: List[str]) -> list:
  """
  Do not return anything, modify s in-place instead.
  """
  left = 0
  right = len(s)-1
  
  while left < right:
    temp = s[left]
    s[left] = s[right]
    s[right] = temp
    left += 1
    right -= 1
    
  return s   

# print(reverseString(['h','e','l','l','o']))

def sortedSquares(nums: List[int]) -> list[int]:
    n = len(nums)
    left = 0
    right = n - 1
    result = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            num = nums[right]
            right -= 1
        else:
            num = nums[left]
            left += 1
        result[i] = num * num
    # below will also work    
    # while left <= right:
    #     if abs(nums[left]) < abs(nums[right]):
    #         num = nums[right]
    #         result[right - left] = num * num
    #         right -= 1
    #     else:
    #         num = nums[left]
    #         result[right - left] = num * num
    #         left += 1    
    return result

print(sortedSquares([-4,-1,0,3,10]))