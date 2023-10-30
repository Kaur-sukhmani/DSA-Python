# linear  Searching 2 D array 

import numpy as np 

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14 ,11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

print(twoDArray)

def searchElement(array, search_element):
    for i in range(len(array)): # O(mn)
        for j in range(len(array[0])): # O(n)
            if search_element == array[i][j]:       # O(1)
                return 'the value is loacted at index '+str(i)+' '+str(j)
    return 'the element not found'
print(searchElement(twoDArray, 18))
            
            