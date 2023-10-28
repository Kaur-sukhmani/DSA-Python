#   list comprehension with condition 
prev_list = [-1,2,-3,4,5,-7]
new_list = [i for i in prev_list if i>0]
print(sum(new_list))

# to tak square of the pnegative number s
new_list=[i*i for i in prev_list if i<0]
print(new_list)

# using funciton in the comprehension 
sentence = 'My name is Love'
def is_consonant(letter):
    vowel = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowel

print(is_consonant('b'))


consonant = [i for i in sentence if is_consonant(i)]
print(consonant)


# new way 
prev_list = [-1,2,-3,4,5,-7]
new_list = [number if number>0 else 0 for number in prev_list]
print(new_list)


# usign fucntion
def get_number(number):
    if number>0:
        return number
    else:
        return 'negative number'
new_list = [get_number(number) for number in prev_list]
print(new_list)  
    