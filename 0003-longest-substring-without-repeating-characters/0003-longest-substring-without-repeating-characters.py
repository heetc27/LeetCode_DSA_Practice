class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) <= 1):
            return len(s)
        maximum_string = 0
        for i in range(len(s)):
            a = []
            for j in range(i, len(s)):
                if s[j] not in a:
                    a.append(s[j])
                    maximum_string = max(maximum_string, len(a))
                else:
                    break
        return maximum_string  