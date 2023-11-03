from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        s = 0
        for j in range(i, n): # ending index
            # add the current element to
            # the subarray a[i...j-1]:
            s += a[j]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == '__main__':
    a = [-1, 1, 1]
    k = 1
    len = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", len)
    
"""Time Complexity: O(N2) approx., where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space."""


###optimal Solution
from typing import List
def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a)
    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        rem = Sum - k
         #Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen
if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")
"""time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array."""