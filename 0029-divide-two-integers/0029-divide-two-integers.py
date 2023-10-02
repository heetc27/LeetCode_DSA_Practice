class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # a=dividend/divisor
        # if dividend == -2**31 and divisor == -1:
        #     return 2**31-1
        # elif a>0:
        #     return floor(a)
        # return ceil(a)
        if not dividend:
            return 0
        sign = 1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            k = 0
            while dividend >= divisor << (k + 1):
                k += 1
            dividend -= (divisor << k)
            res += (1 << k)
        MAX_INT =  (1 << 31) - 1
        return -res if sign else (res if res <= MAX_INT else MAX_INT)
