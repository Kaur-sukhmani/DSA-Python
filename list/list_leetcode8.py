#  Single Number
"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
    """
class Solution:
    def singleNumber(self, nums) -> int:
        num_dict = {}
        for num in nums :
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
            

        for key, value in num_dict.items():
            if value == 1:
                return key 
            
# tc-> O(n)
#  sc->O(n)
# to optimize we will use  XOR fucntion 
class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
# explanation -> ou can solve this problem with a linear runtime complexity
# and constant extra space without using a dictionary. 
# One way to achieve this is by using the XOR bitwise operation. 
# The XOR operation has the property that if you XOR a number with itself, the result is 0. 
# If you XOR 0 with a number, the result is the number itself.

# So, by XORing all the elements in the array, 
# the elements that appear twice will cancel each other out,
# and you'll be left with the single element that appears only once. 
# Here's a modified version of the singleNumber function
"""Time: O(n)
Space: O(1)"""
