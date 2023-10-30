# Linear search

import array
my_array1 = array.array('i', [1, 2, 3, 4, 5])


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target: 
            return i 
    return -1    

print(linear_search(my_array1, 5))
print(linear_search(my_array1, 9))

"""
Time complexity
    def linear_search(array, target):
    for i in range(len(array)):       ----->O(1)
        if array[i] == target:         ----->O(1)
            return i 
    return -1 
    
    SC->O(1)
"""