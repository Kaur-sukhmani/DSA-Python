class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)  # Count the number of zeroes
        nums[:] = [num for num in nums if num != 0]  # Remove zeroes
        nums += [0] * zero_count # Add zeroes to the end
    
obj= Solution()
obj.moveZeroes([0,0,1])
# Move Zeroes
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
        """