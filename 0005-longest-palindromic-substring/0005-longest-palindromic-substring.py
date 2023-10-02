class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0  # Start index of the longest palindrome
        max_length = 1  # Length of the longest palindrome

        for i in range(len(s)):
            # Check for odd-length palindromes
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

            # Check for even-length palindromes
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_length]

