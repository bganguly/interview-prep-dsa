# coding exercise 2:
# max product of two integers
def max_product_unoptimised(arr):
    arr.sort(reverse=False)
    return arr[len(arr)-1] * arr[len(arr)-2]
    # arr.sort(reverse=True)
    # return arr[0]*arr[1]
arr = [1, 7, 3, 4, 9, 5] 
print(max_product_unoptimised(arr)) # Output: 63 (9*7)

# - since the sort above would be NlogN
# better way below - O(n) in time and O(1) in space 
def max_product(arr):
    max1, max2 = 0, 0  
 
    for num in arr:  
        if num > max1:  
            max2 = max1  
            max1 = num  
        elif num > max2:  
            max2 = num  
 
    return max1 * max2  
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)
