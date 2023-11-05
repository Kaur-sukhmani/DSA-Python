"""
1". Two Sum"
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order"""
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print("hello")
            if diff in seen:
                print("returning the list ")
                return [seen[diff], i]
            else:
                print("adding value in the dictionary")
                seen[nums[i]] = i
obj = Solution()
print(obj.twoSum([3, 5, 2, -4, 8, 11], 7))

        
    
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (i != j and nums[i] + nums[j] == target):
        #             return [i, j]
        # return []
# Time complexity: O(N^2);
# Space Complexity: O(1);
        # return_list = []
        # for i in range(0,len(nums)):
        #     diff=int(list[i])-target
        #     for j in range(len(nums),0):
        #         if nums[j] == diff:
        #             return_list.append(i,j)
        #             return
        #         else:
        #             j = j-1

        # nums_indices = {}
        # for i, value in enumerate(nums):
        #     diff = target - value
        #     if diff in nums_indices:
        #         return [nums_indices[diff], i]

        #     nums_indices[value] = i

        # return []