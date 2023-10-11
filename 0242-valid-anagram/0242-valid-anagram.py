class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s = sorted(list(s.strip()))
        list_t = sorted(list(t.strip()))
        if list_s == list_t:
            return True
        else:
            return False


