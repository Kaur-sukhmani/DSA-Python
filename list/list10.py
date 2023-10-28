# Permutation -> same characters but different order 
# first check if the length of the both the list are same or not if not then it is not the permutation of the each other 
def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    # sort both the list 
    list1.sort()
    list2.sort()
    # if after sorting they are equal that means they are permutation of each other else its not 
    # now compare
    if list1 == list2:
        return True
    else:
        return False

# working
list1 = [1,2,3]
list2 = [2,3,1]
print(permutation(list1, list2))
#

# example 2 
list1 = ['a','b','s']
list2 = ['c','b','a']
print(permutation(list1, list2))