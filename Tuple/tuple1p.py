"""Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result) 

# Expected output: 10, 24
"""

def sum_product(input_tuple):
    # TODO
    sum1 = 0 
    product = 1
    for i in input_tuple:
        sum1 += i
        product *= i
    return sum1, product

