class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            sum = 0
            while num:
                sum += num%10
                num = num//10
                
            num = sum

        return num


