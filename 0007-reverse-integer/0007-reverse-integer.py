class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        reversed_num = 0
        while x!=0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        if reversed_num >= 2 ** 31 - 1 or reversed_num <= -2 ** 31:
            return 0
        if isNegative == True:
            return -reversed_num 
        else:
            return reversed_num 
        