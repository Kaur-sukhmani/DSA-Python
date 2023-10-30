# Operations on 1D array 
from array import *


"""1. Create am array and traverse."""
from array import *
arr1 = array('i', [2, 4, 5, 6, 7, 8, 9]) #-> i is integer 
# def Traverse(array):
#     for i in range(len(array)):
#         print(array[i])
# Traverse(arr1)

#  OR
for i in arr1:
    print(i)
    
    
    
"""    
2. Accessing individual elements through indexes"""
print("step 2 ")
print(arr1[0])

"""3. Append any value in an array using insert() method"""
print("step 3")
arr1.append(67)
print(arr1)


"""4. Insert value in an array using insert() method """
print("step 4")
arr1.insert(3, 13)
print(arr1)
#array('i', [2, 4, 5, 13, 6, 7, 8, 9, 67])

"""5.Extend python array using extend() function"""
print("step 5")
my_arr1 = array('i', [10, 11, 12])
arr1.extend(my_arr1)
print(arr1)
#array('i', [2, 4, 5, 13, 6, 7, 8, 9, 67, 10, 11, 12])

"""6. Add items form list into array usign fromlist() method"""
print("step 6")
templist = [20, 21, 22]
arr1.fromlist(templist)
print(arr1)
#array('i', [2, 4, 5, 13, 6, 7, 8, 9, 67, 10, 11, 12, 20, 21, 22])

"""7.remove any array element using remove() method"""
print("step 7")
arr1.remove(67)
print(arr1)

"""8.remove last element using pop() method """
print("step 7")
arr1.pop()
print(arr1)

"""9. fetch any element through its index using index() method """
print("step 9")
print(arr1.index(4))


"""10. reverse a python array using reverse() method"""
print("step 10")
arr1.reverse()
print(arr1)

"""11. get array buffer  information through buffer_info() method """
print("step 11")
print(arr1.buffer_info())
# (140322488706432, 13)

"""12.check for number of occurences of an element usign count() method"""
print("step 12")
arr1.insert(0, 12)
print(arr1)
print(arr1.count(12))

"""13. Convert array to string using tobytes()/fromstrig() method """
print("step 13")
strTemp = arr1.tobytes()
print(strTemp)
ints = array('i') # empty integer array
ints.frombytes(strTemp) # put this array in thsi empty array
print(ints)


"""14. Convert array to a python list with same element usign tolist() method"""
print("step 14")
list_arr = arr1.tolist()
print(list_arr)

"""15 Append a string to char array using fromstring() method"""
print('step 15')

"""16 slice elements from an array """
print("step 16")
arr = arr1[1:4]
print(arr)

