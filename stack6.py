# Special Stack
# Design a Stack that supports getMin() in O(1) time and O(1) extra space.


"""
Design a data-structure SpecialStack that supports all the stack operations
like:
 push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
Your task is to complete all the functions, using stack data-Structure.

Example 1:

Input:
Stack: 18 19 29 15 16
Output: 15
Explanation:
The minimum element of the stack is 15
"""


# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)


# Function should pop an element from stack
def pop(arr):
    if arr:
        arr.pop()


# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return True
    else:
        return False


# function should return 1/0 or True/False
def isEmpty(arr):
    if len(arr) == 0:
        return True
    else:
        return False


# Code here

# function should return minimum element from the stack
def getMin(n, arr):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min


# Code here


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while (not isEmpty(stack)):
            pop(stack)

        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends
