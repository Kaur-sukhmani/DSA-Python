# tuple functions and operators
tuple2 = (1,3,4,5,6,7,8,9)
tuple1 = (5,4,6,8,9,0)
# Concatenation
print(tuple2+tuple1)
# (1, 3, 4, 5, 6, 7, 8, 9, 5, 4, 6, 8, 9, 0)

"""star operator-> create another tuple and each tuple will be multiplied by the number """
print(tuple2 * 2)
# (1, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 5, 6, 7, 8, 9)

"""in operator -> used in searching """
print(4 in tuple2)

"""count()-> count the particular elements in the tuple"""
print(tuple2.count(7))
# 1

"""index()-> tell the index of the elements"""
print(tuple2.index(7)) #5

"""len() function"""
print(len(tuple2)) #8

"""return maximum function"""
print(max(tuple1))
#9

print(min(tuple1))

print(tuple([1,2,3,4]))
#(1, 2, 3, 4)

