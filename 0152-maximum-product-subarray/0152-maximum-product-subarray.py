class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        current = 1
		# left to right pass. Captures all potential subarrays containing first odd n negative numbers
        for i in nums:
            current*=i
            ans = max(ans, current)
			# zero is a delimiter, restart at 1. This is optimal since zero multiplied on is still zero.
            if current == 0:
                current = 1
        current = 1
		# right to left pass capturing all potential subarrays containing last odd n negative numbers
        for i in reversed(nums):
            current*=i
            ans = max(ans, current)
            if current == 0:
                current = 1
        return ans

            