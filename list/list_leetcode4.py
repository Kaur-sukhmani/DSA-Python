class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);
      # 2nd method
        # while k:
        #     i = -1
        #     element = nums.pop(i)
        #     nums.insert(0, element)
        #     i -=1
        #     k -= 1
       
        
obj = Solution()
obj.rotate([1,2,3,4,5,6,7],3)

# ANALYSIS :-

# Time Complexity :- BigO(N)

# Space Complexity :- BigO(1)
# Solution description 


# Qurstion ->Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

"""Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3""" 

"""Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

"K all possible rotation"

[7,1,2,3,4,5,6], k = 1
[6,7,1,2,3,4,5], k = 2
[5,6,7,1,2,3,4], k = 3
[4,5,6,7,1,2,3], k = 4
[3,4,5,6,7,1,2], k = 5
[2,3,4,5,6,7,1], k = 6
[1,2,3,4,5,6,7], k = 7

kay Bonus point what if we have k = -1, then how can we rotate the array. If k is -1 then we have to rotate the value backward not in the front.
Eg - 
Input : [1,2,3,4,5,6,7], k = -1
Output : [2,3,4,5,6,7,1]

Now how did we figure out this, if you carefully look that k = -1 is equals to k = 6.
Just look at the table which I have made for every possible k values

So, what It represent is that add the -ve value to the length of array. And you will get your answer!

"""