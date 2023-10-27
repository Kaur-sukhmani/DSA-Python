"""Tuples"""

"""What is a tuple? How can we create it ?
-> tuple is immutable, hashable(doesnt change), comparable , can be access thougg the integers
-> tuple syntax -> ('','')
"""
# how can we create a tuple ?
"""-> list of values with comma seperated """
tuple = ('a', 'b', 'c', 'd')
print(tuple)
#  ('a', 'b', 'c', 'd')


"""whenever you want to create a single character tuple do like this"""
tuple = ('a', ) 
print(tuple) 
# ('a',)
"""not like this """
tuple = ('a')#this will take it as a single character
print(tuple)
# a

"""can use a tuple() function to declare a tuple """
new_tuple = tuple('abdcd')
print(new_tuple)
# Traceback (most recent call last):
#   File "/Users/sukhm1/Desktop/dsa_python_u/Tuple/tuple1.py", line 24, in <module>
#     new_tuple = tuple('abdcd')
# TypeError: 'str' object is not callable

# TC -> for creating a tuple -> O(1)
# SC -> O(n)
"""Tuples in Memory
Accessing an element of Tuple


Traversing / Slicing a Tuple
Search for an element in Tuple
Tuple Operations/Functions
Tuple vs List
Tuple vs Dictionary
Time and Space complexity of Tuples"""