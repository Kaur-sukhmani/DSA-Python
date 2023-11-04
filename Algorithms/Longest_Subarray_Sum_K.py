#Longest Subarray with sum K | [Postives] 
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
#brute force
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
    a = [2, 3, 5, 1, 9]
    k = 10
    len = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", len)

"""Time Complexity: O(N2) approx., where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space."""


# BEST SLUTION -> optimal 
class Solution:
    def getLongestSubarray(a: [int], k: int) -> int:
        n = len(a) # size of the array.

        left, right = 0, 0 # 2 pointers
        Sum = a[0]
        maxLen = 0
        while right < n:
            # if sum > k, reduce the subarray from left
            # until sum becomes less or equal to k:
            while left <= right and Sum > k:
                Sum -= a[left]
                left += 1

            # if sum = k, update the maxLen i.e. answer:
            if Sum == k:
                maxLen = max(maxLen, right - left + 1)

            # Move forward the right pointer:
            right += 1
            if right < n: Sum += a[right]

        return maxLen



if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")
 
""" Time Complexity: O(2*N), where N = size of the given array.
Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). Now, the inner while loop i.e. the left pointer can move up to the right pointer at most. So, every time the inner loop does not run for n times rather it can run for n times in total. So, the time complexity will be O(2*N) instead of O(N2).

Space Complexity: O(1) as we are not using any extra space."""

