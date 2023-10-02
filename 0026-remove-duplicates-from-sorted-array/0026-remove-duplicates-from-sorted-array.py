class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mlist = list(set(nums))
        mlist.sort()
        for i in range(len(mlist)):
            nums[i] = mlist[i] 
        return len(mlist)
  
  
        