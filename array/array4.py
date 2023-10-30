# Deleting an element

import array
array1 = array.array('i', [1, 2, 3, 4, 5])

array1.remove(5)  #-> TC  while removing the last element -> O(1)
print(array1)

array1.remove(2)  #->  TC while removing other elements -> O(N) and sc -> O(1)
print(array1)