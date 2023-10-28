#Accessing/Traversing the list 


shopping_list = ['Milk', 'chesse', 'butter']


# first method
"""print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])"""

# using in operator we will traverse the list 
# will return true or false 
print('Bread' in shopping_list) #False
print('Milk' in shopping_list) #True
print('Butter' in shopping_list) #False

#traversing from backwards 
print(shopping_list[-1])  #butter

# Traversing the list eith loop
for i in range(len(shopping_list)):
    shopping_list[i] = shopping_list[i]+'+'
    print(shopping_list[i])
    
    
empty = []
for i in empty:
    print("this list is empty ")