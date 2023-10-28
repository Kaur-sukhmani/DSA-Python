# list comprehension 
prev_list= [1,2,3,4,5]
new_list = []
for i in prev_list:
    i1=i*2
    new_list.append(i1)
print(new_list)


# to avoid these many steps we use 
# list comprehension 
prev_list = [24,5,63,2,23]
new_list = [i/3 for i in prev_list]
print(new_list)


# for practive 
language = 'pyhton'
new_list = [i for i in language]
print(new_list)