# Max Consecutive Ones
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 """
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        k = 0
        prev_k = 0
        max_k = 0 
        for element in nums:
            if element == 1:
                k +=1
            else:
                k = 0 
            prev_k = k
            if prev_k > max_k:
                max_k = prev_k
                
        return max_k 
                
obj = Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))
# tc -> O(n)