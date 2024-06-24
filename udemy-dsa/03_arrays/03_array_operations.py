# provide basic array operations incl numpy
# array initialisation
# section 3 - using standard python array
import array
def initialise_array ():
    my_array = array.array('i')
    print(my_array)
    my_array = array.array('i',[-1,0, 1])
    print(my_array)

# section 3 - using numpy
# array initialization - time/space -O(n) for init -no data and that with some data
import numpy as np
def initialise_array_np ():
    np_array = np.array([], dtype=int)
    print(np_array)
    np_array = np.array([-1,0,1])
    print(np_array)
    np_array = np.array([-1,0,'a'])
    print(np_array)

# array insertion - using library array
def array_insert():
    my_array = array.array('i',[-1,0, 1])
    my_array.insert(0,6)

# section 3 - traversal - time/space -O(n)/O(1) 
def traverse_array (array):
    for i in array:
        print(i)
np_array1 = np.array([], dtype=int)
traverse_array(np_array1)
np_array2 = np.array([-1,0,'a'])
traverse_array(np_array2)

# array search  - time/space -O(n)/O(1) 
def search_array(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
my_array = array.array('i',[-1,0, 1])
print(search_array(my_array, 8))

# delete element from array- big-o considerations
# review of all operations above in big-o

# section 3 - two dimensional arrays- initialisation
def initialise_two_dim_array_np():
    twoDArray = np.array([[1],[2],])
    print(twoDArray)
# two dim array- np- insert/access/traverse/search/deletion
# review of all operations for 2 dim above in big-o
# when to use/avoid arrays