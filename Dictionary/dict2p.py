"""Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5
"""
def merge_dicts(dict1, dict2):
    new_dict = {}                             #O(1)
    for key1 in dict1:                        #O(n)
        new_dict[key1] = dict1[key1]          #O(constant)
    for key2 in dict2:                        #O(m)
        if key2 in new_dict:                  #O(cons)
            new_dict[key2] += dict2[key2]     #O(cons)
        else:                                 #O()
            new_dict[key2] = dict2[key2]      #O(cons)      
    return new_dict                           #O()

# TC->O(n+m)
# SC -> O(n+m)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
