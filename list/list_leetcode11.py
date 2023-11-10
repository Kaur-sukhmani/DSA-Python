"""Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""
class Solution:
    def majorityElement(self, nums) -> int:
        dict = {}
        for element in nums :
            if element in dict:
                dict[element] += 1
            else:
                dict[element] = 1
        n = len(nums)//2
        for key, value in dict.items():
            if value > n:
                return key
        return -1
obj = Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))

# TC-> O(N)
# SC-> O(N)

# optimal solution 

        