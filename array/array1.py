# traversing the array

from array import *

arr1 = array( 'i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1, 2, 3, 4, 5, 2])

print(arr1)
print(arr2)

# arr1.insert(2, 9)
# print(arr1)

def traverse(array):
    for i in array:
        print(i, '\n ')
        
""" 
    time complexity 
    def traverse(array):
    for i in array:     -------------------------->  O(n)
        print(i, '\n ') -------------------------->  O(1)
        
    time complexity -> O(n)
    space complexity-> O(1)
"""
        
traverse(arr1)
traverse(arr2)