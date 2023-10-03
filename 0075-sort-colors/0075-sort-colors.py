class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)  
      
        for i in range(length-1):  
            minIndex = i  
            
            for j in range(i+1, length):  
                if nums[j]<nums[minIndex]:  
                    minIndex = j  
                    
            nums[i], nums[minIndex] = nums[minIndex], nums[i]    