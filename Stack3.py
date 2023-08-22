# Delete middle element of a stack
#
"""
Given a stack, delete the middle element of the stack without using any additional data structure.
Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from bottom of the stack.

Note: The output shown by the compiler is the stack from top to bottom.

Stack = {10, 20, 30, 40, 50}
Output:
ModifiedStack = {10, 20, 40, 50}
Explanation:
If you print the stack the bottom-most element will be 10 and the top-most element will be 50.
Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like {10 20 40 50}"""


# User function Template for python3

# User function Template for python3

class Solution:

    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        if sizeOfStack == 0:
            return -1

        # mid = int((sizeOfStack + 1) / 2)
        mid_index = (sizeOfStack + 1) // 2 - 1
        s.pop(mid_index)
        # code here


# {
# Driver Code Starts
# Initial Template for Python 3
import sys

sys.setrecursionlimit(10 ** 8)


def main():
    t = int(input())
    while (t > 0):
        sizeOfStack = int(input())
        myStack = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack, sizeOfStack)
        while (len(myStack) > 0):
            print(myStack[-1], end=" ")
            myStack.pop()
        print()
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
