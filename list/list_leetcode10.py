# Maximum Subarray / KANDANES ALGORITHM
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23

class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:  # Check if the list is empty
            return 0  # Return 0 for an empty list

        currsum = 0
        maxsum = float('-inf')
        for element in nums:
            currsum = max(element, currsum + element)
            maxsum = max(maxsum, currsum)
        return maxsum
            
            
obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))