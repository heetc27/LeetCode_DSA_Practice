class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        if not nums:
            return 0
        if len(nums)<3:
            return 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                three_sum = nums[i]+nums[left]+nums[right]
                if three_sum<target:
                    res = res + right - left
                    left = left+1
                else:
                    right = right - 1
        return res