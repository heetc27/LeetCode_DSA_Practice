class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Empty String
        if not strs:
            return ""

        min_len = min(len(s)for s in strs)
        common_prefix = ""

        for i in range(min_len):
            chars = strs[0][i]
            if all(s[i]==chars for s in strs):
                common_prefix += chars
            else:
                break
        return common_prefix