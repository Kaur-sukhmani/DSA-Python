# check if array is sorted and rotated
"""Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""
class Solution:
    def check(self, nums) -> bool:
        empty_list = sorted(nums) #O(nlogn)
        for element in  nums:  #O(n)
            element1 = nums.pop() #O(1)
            nums.insert(0, element1) #O(1)
            print(nums) #O(1)
            if nums == empty_list:
                return True
        return False
                
            
            
obj = Solution()
obj.check([3,4,5,1,2])

"""Time complexity: O(n^2)

The code iterates through all possible rotations (n rotations), and for each rotation, it checks if the array is sorted (O(n * log(n)) time complexity for sorting). This results in a total time complexity of O(n^2).
Space complexity: O(n)

The code creates a new list for each rotation using slicing (nums[1:] + [nums[0]]) and also creates a sorted copy of the array. Therefore, the space complexity is O(n).
"""
# class Solution:
    # def check(self, nums: List[int]) -> bool:
    #     for i in range (len(nums)):
    #         if nums == sorted(nums):
    #             return True
    #         nums= nums[1 : ] + [nums[0]]
    #     return False

        