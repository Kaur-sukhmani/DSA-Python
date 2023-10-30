# Array Traversal in 2D 

import numpy as np 

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14 ,11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

print(twoDArray)

# len(array)-> len of rows 
def traverseTDArray(array):
    for i in range(len(array)):           # TC O(mn)
        for j in range(len(array[0])):    # TC O(n)
            print(array[i][j])            # TC - O(1)
            
traverseTDArray(twoDArray)