# lists v/s arrays
# similarities
"""1. both data str are mutable
2. both can be indexed and iterated through
3. they can be both sliced"""


#  differemce -> we cant apply arithmetic operatiosn on list

import numpy as np 
myArray = np.array([1,2,3,4,5])
mylist = [1,2,4,5]

print(myArray/2)#->[0.5 1.  1.5 2.  2.5]
print(mylist/2) #->error

#  in array all elememts should be same  but in list there can be diff types of elements 
