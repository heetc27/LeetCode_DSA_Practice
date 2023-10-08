class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        nums.sort()
        if not nums:
            return None
        max_no = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count = count + 1
                if count > max_count:
                    max_count = count
                    max_no = nums[i]
            else:
                count = 1
        return max_no
            
                
                




