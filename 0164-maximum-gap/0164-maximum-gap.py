class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_gap = 0
        nums.sort()
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i-1]
            max_gap = max(max_gap, gap)
            
        return max_gap