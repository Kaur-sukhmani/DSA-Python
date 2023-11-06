class Solution:
    def removeDuplicates(self, nums) -> int:
        count = 0
        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            nums[count] = nums[i]
            count += 1
        return count
        # dict = {}
        # dict_list = []
        # i = 0
        # for element in nums:
        #     if element not in dict:
        #         i = i+1
        #         dict_list.append(element)
        #     dict[element] = True
        # return i,dict_list
obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))