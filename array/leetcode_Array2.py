# Find Second Smallest and Second Largest Element in an array
# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
# tell the brute force approach, better and optimal soltion?

def find_second_smallest_and_second_largest_bruteforce(arr):
    if len(arr) < 2:
        return -1, -1  # Not enough elements

    sorted_arr = sorted(arr)
    return sorted_arr[1], sorted_arr[-2] 
# Time complexity-> O(nlogn)

# optimsl
def find_second_smallest_and_second_largest_optimal(arr):
    if len(arr) < 2:
        return -1, -1  # Not enough elements

    first_smallest = second_smallest = float('inf')
    first_largest = second_largest = float('-inf')

    for element in arr:
        if element < first_smallest:
            second_smallest, first_smallest = first_smallest, element
        elif element > first_largest:
            second_largest, first_largest = first_largest, element
        elif first_smallest < element < second_smallest:
            second_smallest = element
        elif first_largest > element > second_largest:
            second_largest = element

    return second_smallest, second_largest
# tc -> O(n)