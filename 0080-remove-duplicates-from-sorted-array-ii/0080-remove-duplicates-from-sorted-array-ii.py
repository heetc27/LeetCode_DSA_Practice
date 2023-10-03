class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                del nums[i]

        print(nums)
                
        # i = 2
        # while i < len(nums):
        #     if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
        #         del nums[i]
        #     else:
        #         i += 1
        # print(nums)
            

            