# Traversing tuple
tuple = ('a', 'b', 'c', 'd')
for i in tuple:
    print(i)
"""
b
c
d
"""
for i in range(len(tuple)):
    print(i) #0 1 2 3 
    
for i in range(len(tuple)):
    print(tuple[i])   # a b c d 
# Tc-> O(n)
# SC-> O(1)