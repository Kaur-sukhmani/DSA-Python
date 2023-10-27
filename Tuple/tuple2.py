"""Accessing an element of Tuple"""
tuple = ('a', 'b', 'c', 'd')
# located in memory contigiously 
# access through indexing 
# list were accwss using [] square bracket 
# index start from 0
print(tuple[3])#d

# negative indexing is also there 
print(tuple[-3]) #b


"""decond method-> slice operator"""
# syntax = tuple[leftindex:rightindex]
print(tuple[:2])
# ('a', 'b')

print(tuple[1:3]) #('b', 'c')
print(tuple[1:])#('b', 'c', 'd')

"""we cant update the tuples"""