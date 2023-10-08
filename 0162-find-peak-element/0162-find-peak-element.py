class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1 

        for i in range(1, len(nums)-1):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i
            else:
                peak = max(nums)
                for j in range(len(nums)):
                    if nums[j] == peak:
                        return j

                
        