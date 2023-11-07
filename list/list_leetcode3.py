class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j         
# obj = Solution()
# obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# 


# Question
"""Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
# Approach
"""Intuition:
The Intuition is to use two pointers, i and j, to iterate through the array. 
The variable j is used to keep track of the current index where a unique element should be placed. 
The initial value of j is 1 since the first element in the array is always unique and doesn't need to be changed.

Explanation:
The code starts iterating from i = 1 because we need to compare each element with its previous element to check for duplicates.

The main logic is inside the for loop:

If the current element nums[i] is not equal to the previous element nums[i - 1], it means we have encountered a new unique element.
In that case, we update nums[j] with the value of the unique element at nums[i], and then increment j by 1 to mark the next position for a new unique element.
By doing this, we effectively overwrite any duplicates in the array and only keep the unique elements.
Once the loop finishes, the value of j represents the length of the resulting array with duplicates removed.

Finally, we return j as the desired result."""
# TC-> O(n)
# SC-> O(1)