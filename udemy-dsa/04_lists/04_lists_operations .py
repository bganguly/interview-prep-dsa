# list initalisation
shoppingList = ['milk','eggs','cheese','bread']

# iterate via list item values
for item in shoppingList:
    print(item)

# iterate via list item index
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+'+'
    print(shoppingList[i])

# update via index - bigO implications
shoppingList[1] = 'not-eggs'
print(shoppingList)

# inserts via list methods
shoppingList.insert(4,'fish')
shoppingList.append('not-bread')
print(shoppingList)
# append new list to existing list
newShoppingList = ['haldi','dal','chawal']
shoppingList.extend(newShoppingList)
print(shoppingList)

# remove operation when duplicate elements present
shoppingList.append('not-cheese')
shoppingList.append('not-bread')
print(shoppingList)
shoppingList.remove('not-bread') # removes first occurence of element
print(shoppingList)

# slice/delete from list
print(shoppingList[0:2])
print(shoppingList[:2])
print(shoppingList[:]) # original is returned
print(shoppingList[4:])
# pop/delete/remove

# search for elem to exist in list
def isElemInList (elem, list):
    return elem in list
def printElemInList(elem, list):
    # print(f"{elem} in if {isElemInList(elem, list)} else not in") # does not work as expecetd
    suffixStr = 'in list' if isElemInList(elem, list) else 'not in list'
    print(f'{elem} {suffixStr}')
    # if isElemInList(elem, list):
    #     print(f"{elem} in list")
    # else:
    #     print(f"{elem} not in list")

printElemInList('foo', shoppingList)     

# iterate over list elements to search for value
def findElemIndex (elem , list):
    for i, value in enumerate(list):
        if value == elem:
            return i
    return -1
print(findElemIndex('foo', shoppingList))

# standard list operations
# .len(myList)/ .max(myList)
# 4.51 convert string to list and vice versa
# 4.52 common list pitfalls
# 4.53 list vs arrays- arrays are generally used more for arithmetica manipulation
# review of all operations above in big-o

# list comprehension - for list/range/string/tuple
# 4.56 conditional list comprehension
prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [number*number for number in prev_list if number < 0]
print(new_list)

# after 4.56 pracice test 1:
# question 1
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
# a[::3]=10,20,30 - works fine
# a[::2]=10,20,30,40,50,60 - throws error as the replacement to original array will have too many values
# number of elements to replace should match the applicable elemnts (every other number - so exactly 5- not less or more)
print(a)

# question 2
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

# question 3
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])    

# question 4
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1 # changes to list2 will be mirrored in list1
fruit_list3 = fruit_list1[:] # changes to list1 wil not be mirrored in list3
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    # print(ls)
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
    # print(sum)    
 
print(sum)

# question 5
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))

# question 6
import random
fruit=['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)
print(fruit)

# question 7
arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")

# question 8
print()
a=[1,2,3,4,5]
print(a[3:0:-1])