class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(i) for i in digits]
        num = int("".join(s))
        num = num + 1
        num = str(num)
        arr = []
        for i in range(len(num)):
            arr.append(int(num[i]))
        return arr
        


        