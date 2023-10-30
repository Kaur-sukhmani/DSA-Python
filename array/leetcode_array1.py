# Find the Largest element in an array
# Brute force approach 
def find_largest_bruteforce(arr):
    if not arr:
        return None

    largest = arr[0]  # Assume the first element is the largest
    for element in arr:
        if element > largest:
            largest = element

    return largest

# Optimal sol 
def find_largest_optimal(arr):
    if not arr:
        return None

    largest = max(arr)  # Using the max() function to find the largest element
    return largest