# accesing array element 

from array import *

arr1 = array( 'i', [1, 2, 3, 4, 5, 6])

def accessElement(array, index):
    if index >= len(array):
        print("There is not any element in this index")
    else:
        print(array[index])
        
    
"""
Time Complexity->

def accessElement(array, index):
    if index >= len(array):   --------------------------->O(1)
        print("There is not any element in this index") --------------------------->O(1)
    else:
        print(array[index]) --------------------------->O(1)
        
        TC->O(1)
        SC->O(1)
"""    
accessElement(arr1, 5)
accessElement(arr1, 7)