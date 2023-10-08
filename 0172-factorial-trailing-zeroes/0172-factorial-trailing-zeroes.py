class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        co = 0
        while n > 0:
            co+= n // 5
            n //= 5
        return co
