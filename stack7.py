# Next Greater Element

"""
Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array
in order of their appearance in the array.
Next greater element of an element in the array is the nearest element
on the right which is greater than the current element.

If there does not exist next greater of current element, then next greater element for current element is -1.
 For example, next greater of the last element is always -1.

Example 1:

Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.
"""


# User function Template for python3


class Solution:
    def nextLargerElement(self, arr, n):
        res = []
        for i in range(n):
            j = i + 1
            while j < n:
                if arr[j] > arr[i]:
                    res.append(arr[j])
                    break
                j += 1
            if j == n:
                res.append(-1)
        return res
        # takes a large amont of time so insteas
    """    if len(arr) == 0:
            return -1
        res = [-1] * n
        for i in range(len(arr)):
            j = i+1
            while j < n:
                if arr[j] > arr[i]:
                    res.append(arr[j])

                j += 1
        return res """










# code here


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())

        a = list(map(int, input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
