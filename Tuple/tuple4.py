# Searching for an element in tuple
tuple = ('a', 'b', 'c', 'd')
print('a' in tuple) # in operator -> return boolean variable 
# True
print('g' in tuple)
# False

# TC-> O(N)
"""index method"""
print(tuple.index('c'))
# ->TC->O(n)
# 2

"""defing a function"""
def search_element(tuple_ex, element_ex):
    for i in range(len(tuple_ex)):        #->O(N)
        if tuple_ex[i] == element_ex:#O(1)
            return f"this {element_ex} is found at {i} index"#O(1)
    return f"the {element_ex} not found"#O(1)
print(search_element(tuple, 'd'))#O(N)
# SC-> O(1)
#op-> this d is found at 3 index

