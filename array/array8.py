# accessing elements of 2D array 
import numpy as np 

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14 ,11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

print(twoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):  # TC-> O(1)
        print("Incorrect Index ")     #TC O(1)
    else:
        print(array[rowIndex][colIndex])   #TC O(1)
        # SC - O(1)
accessElements(twoDArray, 2, 3)


        
        
        