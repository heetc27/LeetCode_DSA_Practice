import numpy as np
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            if nums.count(i)==1:
                l.append(i)
            if len(l)==2:
                return l
        


