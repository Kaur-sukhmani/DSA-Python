"""Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output:

{1: 'a', 2: 'b', 3: 'c'}
"""
def reverse_dict(my_dict):
    # TODO
    dict1 = {}
    
    for key, value in my_dict.items():
        # dict1 = ict(my_dict[key]= key)
        dict1[value] = key
    return dict1
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))


# ALT
def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}
