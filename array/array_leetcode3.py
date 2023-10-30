# Linear Search
def linearSearch(n: int, num: int, arr: [int]) -> int:
    if n==0:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i]== num:
                return i
        return -1
# linearSearch(5, 4,[6,7,8,4,11] )

# Ques 
"""You are given an array 'arr' containing 'n' integers. You are also given an integer 'num' and your task is to find whether
'num' is present in the array or not.
If 'num' is present in the array, return the O-based index of the first occurrence of 'num'. Else, return - 1.
Example:
Input: 'n' = 5, 'num' = 4
'arr' = [6,7,8,4,11]
Output: 3
Explanation:
4 is present at the 3rd index.
Detailed explanation ( Input/output format, Notes, Images
Sample Input 1:
5 4
6 7 8 4 1"""