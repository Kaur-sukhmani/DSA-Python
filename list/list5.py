# list operators/functions 
"""a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)"""
# can concatenate two list together


# *operator 
a = [0, 1]
a = a*4
print(a)
# by using * operator we repeat the things 

# len ->to count the number of elements 
a = [1, 2, 3, 4, 5, 6, 7, 8, 22]
print(len(a))

# max()-> returns the item with the highest value in the list 
print(max(a))

# min()-> returns the item with the lowest value in the list 
print(min(a))

# sum()-> returns the sum of all items in the list
print(sum(a))
"""from sum can calculate the average of the list """
average = sum(a)/len(a)
print("averge of the list is ->{}".format(average))


total = 0
count = 0
while(True):
    inp = input("Enter a number:")
    if inp == 'done':
        break
    value = float(inp)
    total = total + value 
    count = count + 1
    average = total/count
    
print("Average:", average)

# to calculate the average of the list 
mylist = list()
while(True):
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    mylist.append(value)
average = sum(mylist)/len(mylist)

print('Average:', average)