""" 
Subarray Sum Equals K
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        mp = {}
        cnt = 0
        for i in range(n):
            if prefix[i] == k:
                cnt += 1
            if prefix[i] - k in mp:
                cnt += mp[prefix[i] - k]
            print("mp.get(prefix[i], 0)", mp.get(prefix[i], 0))
            mp[prefix[i]] = mp.get(prefix[i], 0) + 1
        return cnt 
    
obj = Solution()
print(obj.subarraySum([1,1,1],2))
# print(obj.subarraySum([1,2,3],3))
