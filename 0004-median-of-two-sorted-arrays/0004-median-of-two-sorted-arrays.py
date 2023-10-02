class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = 0
        merged_array = nums1 + nums2
        merged_array.sort() 
        mid = (len(merged_array)/2) 
        for i in range(len(merged_array)):
            for j in range(i, len(merged_array)):
                if (len(merged_array) % 2) == 1:
                    median = merged_array[(len(merged_array))//2]
                elif (len(merged_array) % 2) == 0:
                    median = (merged_array[mid - 1] + merged_array[mid]) / 2.0
        return median