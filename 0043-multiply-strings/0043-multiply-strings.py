class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0;
        m1 = 1;
        i = len(num1) -1
        while i >= 0:
            j = len(num2) -1
            m2 = 1
            while j >= 0:
                result += int(num1[i]) * m1 * int(num2[j]) * m2
                m2 *= 10
                j-=1
            m1 *= 10
            i-=1
        return str(result)