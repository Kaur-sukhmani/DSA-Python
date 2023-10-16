# searchingn for an element
my_list = [100,200,300,400,500]
# using in operator 
target = 500
"""if target in my_list:
    print(f"{target} is in the list ")
else:
    print(f"{target} is not in the list ")
    
"""
#  linear search
def linear_search(plist,ptarget):
    for i, value in enumerate(plist):   #------>O(n)
        if value == ptarget:              #------>O(1)
            return i                    #------>O(1)
    return -1                           #------>O(1)

print(linear_search(my_list, target))
