import math
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        
        closest_sum = float('inf')
        for i in range(N - 2):
            left = i + 1
            right = N - 1
            
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum
                
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return closest_sum
        
        return closest_sum








