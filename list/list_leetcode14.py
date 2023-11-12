"""
Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according 
to their lexicographical order, then the next permutation of that array is the permutation 
that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order 
(i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
"""
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # approach -> we will take 2 pointers from end , 
        # and we will put the i at the where ever the the element i-1 is smaller then the i element 
        # and j where the first element greator than the i elemnt 
        i = j = len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        if i==0:
            nums.reverse()
            return
        while nums[j]<=nums[i-1]:
            j-=1
        # swap 
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # revserse the list 
        nums[i:] = nums[len(nums)-1:i-1:-1]

        # To find next permutations, we'll start from the end
        # i = j = len(nums)-1
        # # First we'll find the first non-increasing element starting from the end
        # while i > 0 and nums[i-1] >= nums[i]:
        #     i -= 1
        # # After completion of the first loop, there will be two cases
        # # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        # if i == 0:
        #     nums.reverse()
        #     return 
        # # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        # while nums[j] <= nums[i-1]:
        #     j -= 1
        # # Now out pointer is pointing at two different positions
        # # i. first non-assending number from end
        # # j. first number greater than nums[i-1]
        
        # # We'll swap these two numbers
        # nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        # nums[i:]= nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place
        return nums 


        
obj = Solution()
print(obj.nextPermutation([6, 2, 1, 5, 4, 3, 0]))
        