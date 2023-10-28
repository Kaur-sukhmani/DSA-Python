# update/insert - list 

mylist = [1, 2, 3, 4, 5, 6, 7]
print(mylist)

# upadte the list  usign bracket operator 
mylist[3]=23   #----->tc =O(1)  sc=O(1)
print(mylist)

# insereting elements 
"""# iserting an element to the beginnning of the list 
# inserting an element to the any given place in the list 
# insertign an element to the end of the list
# inserting another list to the list """


# to insert an element use list method 
"""1) insert()
   2) append()
   3) extend()
"""

# insert(index_to_insert, value_of_index) -> can insert any value at any index 
list = [1, 2, 3, 4, 5, 6, 7]

list.insert(0, 23)
print(list)

list.insert(3,26)        #------------------>O(n)
print(list)

# appnend -> can only insert values at the end  of the list 
list.append(55)            #---------------->O(1)
print(list)


# extend() -> can add one list to another list 
list2 = [5, 6, 7, 8, 9, 10]
list.extend(list2)         #-----------------> O(n)
print(list)
